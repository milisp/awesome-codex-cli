const test = require('node:test');
const assert = require('node:assert/strict');
const { fields, canonical, inspect } = require('../scripts/validate-submission.cjs');

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
