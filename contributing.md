# Contributing

External contributions are welcome through **issues only**. Pull request creation is restricted to collaborators in repository settings; maintainers use PRs to maintain the repository.

1. Read the inclusion criteria below and check the README and existing issues for duplicates.
2. Open an issue using **Submit a resource** or **Report a correction**.
3. For new resources, provide a project link, suggested section, factual description, Codex integration evidence, and verifiable external usage evidence.
4. Maintainers review the issue and update the list if accepted. Submission does not guarantee inclusion.

Resource issues receive automated field, evidence-link, and duplicate-URL checks. The bot reports GitHub stars and archive status in a summary table, and updates its result when you edit the issue. A project under 100 stars gets `manual-review`; the bot never closes an issue. `validation-passed` means basic checks passed, not approval or verification of the evidence. Missing information gets `needs-evidence` or `needs-changes`; archived repositories and failed metadata queries get `manual-review`. The bot does not decide inclusion; maintainers apply the inclusion criteria below.

## Contribute Codex Commands, Workflows, and Templates

Have a useful Codex slash command guide, reusable prompt/template, skill, plugin, or end-to-end workflow? Please submit a resource issue and suggest the matching section of `README.md`. Include the project link and a concise, factual description of what it does and how it works with Codex. For commands and templates, link directly to the files or documentation when possible.

New resources are automatically recorded in `RECENTLY_ADDED.md` after maintainers add them to main. Contributors do not need to edit that file. Description edits and category moves are not recorded as new additions.

The ticker samples GitHub projects separately; ticker placement does not replace review and inclusion in the curated list.

## 🚀 Launch Your Agent, MCP Server, or Skill

Built an MCP Server, Agent Skill, or Micro-SaaS for Codex CLI?

- **Showcase & Get Traffic**: Submit your build to **[productship.lol](https://productship.lol)** to reach the AI developer community and get featured.
- **Inclusion Criteria below**: Once your tool meets the criteria below, feel free to submit a resource issue for consideration in `README.md`.

## Inclusion Criteria

A resource must meet **all** of the following.

1. **Adoption.** It has at least 100 GitHub stars. Age alone does not qualify. A resource below 100 stars is reviewed individually: the submission must explain what makes it distinct from existing entries and why Codex CLI users need it, and a maintainer decides on quality.
2. **Codex support.** It works with Codex CLI, shown by code or documentation, not only a line in its README.
3. **Open access.** Closed-source projects, and projects that need a sign-up or payment, are judged only on signals from other users (stars, downloads, third-party listings), not on the author's claims. A paid tier does not rule out a free, public core that works without an account.
4. **Scope.** The resource must be usable from Codex CLI. An MCP server qualifies when its documentation gives a working Codex setup, such as a `codex mcp add` command or a `config.toml` block. Servers that work with any MCP client qualify under this rule, provided they document that setup.
5. **Entry style.** One resource per issue, with one entry, one section, and one factual line on what it does. Keep the tone neutral. Issues that bundle several resources must be split.

Submissions that miss these criteria are not merged. Being submitted does not guarantee inclusion, and a maintainer may decline one without a full review.

No users yet? Submit once you meet the criteria.
