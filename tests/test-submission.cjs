const test = require('node:test');
const assert = require('node:assert/strict');
const { fields, canonical, inspect, criteria } = require('../scripts/validate-submission.cjs');

const body = `### Project name and URL
Tool https://github.com/example/tool
### Suggested README section
Tools
### Factual description
A Codex helper.
### Codex integration evidence
https://github.com/example/tool/blob/main/README.md
### External usage evidence
https://example.com/usage
### Your relationship to the project
User
### Checklist
- [x] First
- [X] Second
- [x] Third
`;

test('parses complete form including final field and CRLF', () => {
  assert.match(fields(body.replaceAll('\n', '\r\n')).Checklist, /Third/);
  assert.deepEqual(inspect(body, ''), {
    evidence: [], changes: [], repository: { owner: 'example', repo: 'tool' },
  });
});
test('normalizes GitHub URLs and catches duplicate', () => {
  assert.equal(canonical('https://github.com/Example/Tool.git/'), 'github.com/example/tool');
  assert.equal(inspect(body, '[Tool](https://github.com/example/tool/)').changes.length, 1);
});
test('requires evidence links, missing fields and checked checklist', () => {
  const result = inspect('### Project name and URL\n_No response_\n', '');
  assert.ok(result.evidence.length >= 6);
  assert.equal(result.changes.length, 1);
});
test('does not treat low stars or age as a local rejection rule', () => {
  assert.deepEqual(inspect(body, '').changes, []);
});
test('meets criteria at 100 stars or 14 days old, otherwise reports both numbers', () => {
  assert.equal(criteria({ stars: 100, ageDays: null }).met, true);
  assert.equal(criteria({ stars: 52, ageDays: 14 }).met, true);
  assert.equal(criteria({ stars: 52, ageDays: 13.9 }).met, false);
  const below = criteria({ stars: 3, ageDays: null });
  assert.equal(below.met, false);
  assert.match(below.reason, /3 stars < 100 and age unknown < 14 days/);
});
