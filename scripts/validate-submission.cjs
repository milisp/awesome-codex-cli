const fs = require('node:fs');

const LABELS = {
  'resource-submission': ['0366d6', 'Resource proposed for inclusion'],
  correction: ['5319e7', 'Correction to an existing entry'],
  'validation-pending': ['ededed', 'Awaiting automated checks'],
  'validation-passed': ['0e8a16', 'Basic checks passed; not approval'],
  'needs-evidence': ['fbca04', 'Required submission evidence is missing'],
  'needs-changes': ['d93f0b', 'Basic submission checks need attention'],
  'manual-review': ['c5def5', 'Needs maintainer review'],
};
const STATUS = ['validation-pending', 'validation-passed', 'needs-evidence', 'needs-changes', 'manual-review'];
const MARKER = '<!-- submission-validation -->';
const REQUIRED = ['Project name and URL', 'Suggested README section', 'Factual description',
  'Codex integration evidence', 'External usage evidence', 'Your relationship to the project'];

function fields(body) {
  const result = {};
  for (const match of body.matchAll(/^### ([^\r\n]+)\r?\n([\s\S]*?)(?=^### |$(?![\s\S]))/gm)) {
    result[match[1].trim()] = match[2].trim();
  }
  return result;
}

function urls(text) {
  return (text.match(/https?:\/\/[^\s<>]+/gi) || []).map(s => s.replace(/[),.;]+$/, ''));
}

function canonical(raw) {
  try {
    const url = new URL(raw);
    const path = url.pathname.replace(/\/$/, '').replace(/\.git$/, '');
    return `${url.hostname.toLowerCase()}${path}`.toLowerCase();
  } catch { return null; }
}

function inspect(body, readme) {
  const data = fields(body);
  const evidence = [], changes = [];
  for (const name of REQUIRED) {
    if (!data[name] || data[name] === '_No response_') evidence.push(`Missing field: ${name}.`);
  }
  for (const name of ['Codex integration evidence', 'External usage evidence']) {
    if (!urls(data[name] || '').length) evidence.push(`Provide a public evidence URL in ${name}.`);
  }
  const project = urls(data['Project name and URL'] || '')[0];
  if (!project) evidence.push('Provide a project URL.');
  const existing = new Set(urls(readme).map(canonical));
  if (project && existing.has(canonical(project))) changes.push('The project URL is already in README.md.');
  const checklist = data.Checklist || '';
  if ((checklist.match(/^- \[[xX]\]/gm) || []).length < 3) changes.push('Complete all three checklist items.');
  let repository = null;
  if (project) {
    const url = new URL(project);
    if (url.hostname.toLowerCase() === 'github.com') {
      const parts = url.pathname.split('/').filter(Boolean);
      if (parts.length >= 2) repository = { owner: parts[0], repo: parts[1].replace(/\.git$/, '') };
    }
  }
  return { evidence, changes, repository };
}

async function run({ github, context }) {
  const repo = context.repo;
  for (const [name, [color, description]] of Object.entries(LABELS)) {
    try { await github.rest.issues.getLabel({ ...repo, name }); }
    catch (error) {
      if (error.status !== 404) throw error;
      try { await github.rest.issues.createLabel({ ...repo, name, color, description }); }
      catch (createError) { if (createError.status !== 422) throw createError; }
    }
  }
  if (!context.payload.issue) return; // Manual run bootstraps labels before submissions.
  const issue_number = context.payload.issue.number;
  const { data: issue } = await github.rest.issues.get({ ...repo, issue_number });
  if (issue.pull_request || issue.state !== 'open') return;
  const names = issue.labels.map(label => typeof label === 'string' ? label : label.name);
  const resource = names.includes('resource-submission') || issue.title.startsWith('[Resource]');
  if (!resource) {
    if (issue.title.startsWith('[Correction]')) {
      await github.rest.issues.addLabels({ ...repo, issue_number, labels: ['correction'] });
    }
    return;
  }
  const result = inspect(issue.body || '', fs.readFileSync('README.md', 'utf8'));
  const notes = [];
  let manual = false;
  if (result.repository) {
    try {
      const { data: target } = await github.rest.repos.get(result.repository);
      notes.push(`GitHub metadata: **${target.stargazers_count} stars**; archived: **${target.archived ? 'yes' : 'no'}**.`);
      if (target.archived) { manual = true; notes.push('Archived projects require maintainer review.'); }
    } catch {
      manual = true;
      notes.push('GitHub metadata could not be retrieved. A maintainer must check it; this is not a rejection.');
    }
  }
  const labels = ['resource-submission'];
  if (result.evidence.length) labels.push('needs-evidence');
  if (result.changes.length) labels.push('needs-changes');
  if (manual) labels.push('manual-review');
  if (!result.evidence.length && !result.changes.length && !manual) labels.push('validation-passed');
  // Remove only our obsolete status labels; preserve unrelated maintainer labels.
  for (const name of STATUS.filter(name => names.includes(name) && !labels.includes(name))) {
    try { await github.rest.issues.removeLabel({ ...repo, issue_number, name }); }
    catch (error) { if (error.status !== 404) throw error; }
  }
  await github.rest.issues.addLabels({ ...repo, issue_number, labels });
  const problems = [...result.evidence, ...result.changes];
  const body = `${MARKER}\n## Submission checks\n\n` +
    (problems.length ? problems.map(s => `- ${s}`).join('\n') : 'Required fields and basic duplicate checks passed.') +
    (notes.length ? '\n\n' + notes.join('\n\n') : '') +
    '\n\nThese are basic checks, not verification of project quality or approval for inclusion. No stars or age cutoff is applied. Edit this issue to rerun checks.';
  const comments = await github.paginate(github.rest.issues.listComments, { ...repo, issue_number, per_page: 100 });
  const previous = comments.find(c => c.user.login === 'github-actions[bot]' && c.body?.includes(MARKER));
  if (previous) await github.rest.issues.updateComment({ ...repo, comment_id: previous.id, body });
  else await github.rest.issues.createComment({ ...repo, issue_number, body });
}

module.exports = { fields, canonical, inspect, run };
