# Awesome Codex CLI 🚀

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/milisp/awesome-codex-cli?style=social)](https://github.com/milisp/awesome-codex-cli/stargazers)
[![Follow on 𝕏](https://img.shields.io/badge/𝕏-@lisp__mi-1c9bf0)](http://x.com/intent/follow?screen_name=lisp_mi)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/codex?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/codex/)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/zAjtD4kf5K)

A curated list of Agent skill, awesome resources, tools, and tutorials for OpenAI Codex CLI

- [Features](#features)
- [Agent Skills](#agent-skills)
  - [General](#general)
- [Workflows & Knowledge Guides](#workflows--knowledge-guides-)
- [Tools](#tools)
  - [GUI & MCP](#gui--mcp)
  - [setup tool](#setup-tool)
  - [Session manager](#session-manager)
  - [WebUI \& App](#webui--app)
  - [Development Tools](#development-tools)
  - [Stat](#stat)
    - [Editor](#editor)
    - [Termial](#termial)
    - [System](#system)
- [Official Resources](#official-resources)
  - [Documentation](#documentation)
  - [Blog Posts & Tutorials](#blog-posts--tutorials)
- [GUI & Web Interface Extensions](#gui--web-interface-extensions)
  - [Official Web Interface](#official-web-interface)
  - [IDE Integrations](#ide-integrations)
- [Use Cases](#use-cases)
  - [Development Tasks](#development-tasks)
  - [Specialized Tasks](#specialized-tasks)
- [Community](#community)
  - [Discussions](#discussions)
  - [Learning Resources](#learning-resources)
  - [Community Projects](#community-projects)
- [Contributing](#contributing)
- [License](#license)

## What is OpenAI Codex CLI?

[OpenAI Codex CLI](https://github.com/openai/codex) is Lightweight coding agent that runs in your terminal

## Features

- [codexia](https://github.com/milisp/codexia) - Agent workstation for Codex CLI and Claude Code

## Agent Skills

> Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

### General

- [Agents.md](https://agents.md) - A simple, open format for guiding coding agents, used by over 20k open-source projects.
- [Codex Skills](https://github.com/openai/skills) - Skills Catalog for Codex
- [Codex Skills](https://github.com/Dimillian/Skills) - Codex Skills by Dimillian
- [Ariadne Loop](https://github.com/zhangzeyu99-web/ariadne-loop) by [Aaron Zhang](https://github.com/zhangzeyu99-web) - Codex skill and CLI for turning GitHub issues, release plans, refactors, and handoffs into verifiable Loop Engineering specs with inspect-act-verify-decide gates.
- [AgentSys](https://github.com/avifenesh/agentsys) by [avifenesh](https://github.com/avifenesh) - Workflow automation system for Claude with a group of useful plugins, agents, and skills. Automates task-to-production workflows, PR management, code cleanup, performance investigation, drift detection, and multi-agent code review. Includes [agnix](https://github.com/avifenesh/agnix) for linting agent configurations. Built on thousands of lines of code with thousands of tests. Uses deterministic detection (regex, AST) with LLM judgment for efficiency. Used on many production systems.
- [AI Agent, AI Spy](https://youtu.be/0ANECpNdt-4) by [Whittaker & Tiwari](https://signalfoundation.org/) - Members from the Signal Foundation with some really great tips and tricks on how to turn your operating system into an instrument of total surveillance, and why some companies are doing this really awesome thing. [warning: YouTube link].
- [cc-devops-skills](https://github.com/akin-ozer/cc-devops-skills) by [akin-ozer](https://github.com/akin-ozer) - A practical agent skill pack for DevOps work in Claude Code and Codex.
- [Claude Codex Settings](https://github.com/fcakyon/claude-codex-settings) by [fatih akyon](https://github.com/fcakyon) - A well-organized, well-written set of plugins covering core developer activities, such as working with common cloud platforms like GitHub, Azure, MongoDB, and popular services such as Tavily, Playwright, and more. Clear, not overly-opinionated, and compatible with a few other providers.
- [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) by [K-Dense](https://github.com/K-Dense-AI/) - "A set of ready-to-use Agent Skills for research, science, engineering, analysis, finance and writing." That's their description - modest, simple. That's how you can tell this is really one of the best skills repos on GitHub. If you've ever thought about getting a PhD... just read all of these documents instead. Also I think it IS an AI agent or something? Awesome.
- [Codex Skill](https://github.com/skills-directory/skill-codex) by [klaudworks](https://github.com/klaudworks) - Enables users to prompt codex from claude code. Unlike the raw codex mcp server, this skill infers parameters such as model, reasoning effort, sandboxing from your prompt or asks you to specify them. It also simplifies continuing prior codex sessions so that codex can continue with the prior context.
- [Compound Engineering Plugin](https://github.com/EveryInc/compound-engineering-plugin) by [EveryInc](https://github.com/EveryInc) - A very pragmatic set of well-designed agents, skills, and commands, built around a discipline of turning past mistakes and errors into lessons and opportunities for future growth and improvement. Good documentation.
- [Context Engineering Kit](https://github.com/NeoLabHQ/context-engineering-kit) by [Vlad Goncharov](https://github.com/LeoVS09) - Hand-crafted collection of advanced context engineering techniques and patterns with minimal token footprint focused on improving agent result quality.
- [Everything OpenAI Codex](https://github.com/mturac/everything-openai-codex) by [Mehmet Turac](https://github.com/mturac) - Open-source Codex workflow system with agents, skills, commands, hooks, memory patterns, install profiles, and validation checks for repeatable coding sessions.
- [read-only-postgres](https://github.com/jawwadfirdousi/agent-skills) by [jawwadfirdousi](https://github.com/jawwadfirdousi) - Read-only PostgreSQL query skill for Claude Code. Executes SELECT/SHOW/EXPLAIN/WITH queries across configured databases with strict validation, timeouts, and row limits. Supports multiple connections with descriptions for database selection.
- [Superpowers](https://github.com/obra/superpowers) by [Jesse Vincent](https://github.com/obra) - A strong bundle of core competencies for software engineering, with good coverage of a large portion of the SDLC - from planning, reviewing, testing, debugging... Well written, well organized, and adaptable. The author refers to them as "superpowers", but many of them are just consolidating engineering best practices - which sometimes does feel like a superpower when working with Claude Code.
- [Trail of Bits Security Skills](https://github.com/trailofbits/skills) by [Trail of Bits](https://github.com/trailofbits) - A very professional collection of over a dozen security-focused skills for code auditing and vulnerability detection. Includes skills for static analysis with CodeQL and Semgrep, variant analysis across codebases, fix verification, and differential code review.
- [TÂCHES Claude Code Resources](https://github.com/glittercowboy/taches-cc-resources) by [TÂCHES](https://github.com/glittercowboy) - A well-balanced, "down-to-Earth" set of sub agents, skills, and commands,  that are well-organized, easy to read, and a healthy focus on "meta"-skills/agents, like "skill-auditor", hook creation, etc. - the kind of things you can adapt to your workflow, and not the other way around.
- [Web Assets Generator Skill](https://github.com/alonw0/web-asset-generator) by [Alon Wolenitz](https://github.com/alonw0) - Easily generate web assets from Claude Code including favicons, app icons (PWA), and social media meta images (Open Graph) for Facebook, Twitter, WhatsApp, and LinkedIn. Handles image resizing, text-to-image generation, emojis, and provides proper HTML meta tags.
- [These are the rules](https://x.com/kregenrek/status/1965113557160484961) to make code search faster and more accurate. - [Kevin Kern](https://x.com/kregenrek)
- [Diffmode Growth Tactics](https://github.com/acogood/diffmode_free) by [Anton Kogut](https://github.com/acogood) - A growth-strategy skill pack for Codex and Claude Code: point it at a product URL and it researches your competitors and buyers, then writes 7-9 unconventional acquisition tactics (synthesis.md), each fusing 2-3 growth mechanisms from fresh case studies. Reviewer-gated, Apache-2.0, Perplexity-optional.

## Workflows & Knowledge Guides 🧠

> A workflow is a tightly coupled set of Codex-native resources that facilitate specific projects

- [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) - OmX - Oh My codeX: Your codex is not alone. Add hooks, agent teams, HUDs, and so much more.

## Tools

### GUI & MCP
- [codexia-zen](https://github.com/milisp/codexia-zen) - a minimalist design GUI for OpenAI Codex CLI
- [MCP Linker](https://github.com/milisp/mcp-linker) - GUI for managing MCP configs for Codex CLI
- [x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper) - X/Twitter data extraction skill & MCP server for AI coding agents. 20 tools: followers, tweets, replies, mentions, lists, hashtags, spaces & more.

### MCP server
- [prompt-to-asset](https://github.com/MohamedAbdallah-14/prompt-to-asset) - MCP server that generates app icons, favicons, OG images, logos, and wordmarks by routing requests across 30+ image generation models. Zero API key needed on first run via free-tier providers.
- [ejentum-mcp](https://github.com/ejentum/ejentum-mcp)
- [click-to-mcp](https://github.com/Coding-Dev-Tools/click-to-mcp) - Auto-wrap any Python Click/Typer CLI as an MCP server. Zero-code transformation that introspects CLI commands and exposes them as MCP tools. Works with Codex CLI, Claude Code, and any MCP client. `pip install click-to-mcp` - Reasoning Harness MCP server. Library of 679 cognitive operations engineered in natural language across four harnesses (reasoning, code, anti-deception, memory). Each call retrieves a task-matched scaffold (failure pattern, procedure, suppression vectors, falsification test) the agent ingests before responding. Free tier 100 calls.

### setup tool
- [codex-1up](https://github.com/regenrek/codex-1up) - equips your Codex CLI coding agent with powerful tools.
- [codex-universal](https://github.com/openai/codex-universal) - Base docker image used in Codex environments

### Session manager
- [crystal](https://github.com/stravu/crystal) - Run multiple Codex and Claude Code AI sessions in parallel git worktrees. Test, compare approaches & manage AI-assisted development workflows in one desktop app.
- [Parallel Code](https://github.com/johannesjo/parallel-code) - Desktop app for running Codex CLI, Claude Code, and Gemini CLI agents side by side in separate git worktrees.
- [vibe-kanban](https://github.com/BloopAI/vibe-kanban) - Kanban board to manage your AI coding agents
- [ccmanager](https://github.com/kbwo/ccmanager) - Coding Agent Session Manager that supports Claude Code / Gemini CLI / Codex CLI / Cursor Agent / Copilot CLI
- [codmate](https://github.com/loocor/codmate) - a macOS SwiftUI app for managing CLI AI sessions
- [agent-sessions](https://github.com/jazzyalex/agent-sessions) - Local-first macOS app for browsing and full-text searching Codex session history alongside other local coding-agent transcripts; resume is available where the underlying CLI supports it.
- [codexsm](https://github.com/milisp/codexsm) - Codex session manager, Cross platform GUI. rename, view, delete session file. one click resume session
- [agentbox](https://github.com/madarco/agentbox) - Run multiple Codex (and Claude Code / OpenCode) sessions in parallel, each in its own sandboxed box — local Docker or cloud VMs (Hetzner/Daytona/Vercel/E2B). Sub-1s checkpoint starts, per-box browser + VS Code, and a dashboard to switch between boxes.

### WebUI & App
- [happy](https://github.com/slopus/happy) - Mobile and Web client for Codex and Claude Code, with realtime voice, encryption and fully featured
- [CodexMonitor](https://github.com/Dimillian/CodexMonitor) - An app to monitor the (Codex) situation
- [CodexFlow](https://github.com/lulu-sk/CodexFlow) - CodexFlow is an enhanced GUI tool designed for Codex CLI, focused on improving conversation management and interaction.
- [Codex-webui](https://github.com/harryneopotter/Codex-webui) - A minimal webui to run Codex-CLI locally with a UI, session resume and persistent memory (Un-official)
- [AionUi](https://github.com/iOfficeAI/AionUi) - Free, local, open-source GUI app for Gemini CLI — Better Chat UI, File Management, AI image editing, multi-agent support, multi-LLMs
- [Untether](https://github.com/littlebearapps/untether) - Telegram bridge for Codex CLI (and 5 other agents). Send tasks by voice, stream progress, toggle approval policy (full auto/safe) via inline buttons
- [IM.codes](https://github.com/im4codes/imcodes) - The IM for agents: a mobile/web control layer for Codex CLI and other terminal-based coding agents, with terminal access, file browsing, git views, localhost preview, notifications, and multi-agent workflows.
- [Onepilot](https://onepilotapp.com) - Native iOS SSH terminal for Codex CLI and Claude Code. Full PTY, GitHub integration, localhost forwarding, live file editing, and one-click AI agent deployment via OpenClaw. [App Store](https://apps.apple.com/app/onepilot-ai-terminal/id6743826919).
- [ToutKit](https://github.com/toutkit/toutkit) - Desktop notebook with a built-in terminal that runs Codex CLI alongside Claude Code and Gemini; an in-app webview renders whatever the agent writes inline, and each note is a self-contained folder with its own SQLite, files, and scripts. Local-first, Electron, AGPL-3.0.

### Development Tools
- [humanlayer](https://github.com/humanlayer/humanlayer) - The best way to get AI coding agents to solve hard problems in complex codebases.
- [Agent FM](https://github.com/agentfm-ai/agent-fm) - Local macOS app for listening to Claude Code and Codex agents, with Global Mix, blocker alerts, and BYOK narration.
- [EchoCoding](https://github.com/launsion-boop/EchoCoding) - Audio layer for Codex CLI with hook-triggered SFX, ambient soundscape, and optional cloud TTS/ASR voice interaction.
- [unslop](https://github.com/MohamedAbdallah-14/unslop) - CLI and MCP server that removes AI writing patterns from agent-generated text. Works with Codex, Claude Code, Gemini CLI, and Cursor. Five intensity levels and lint-only audit mode.
- [brooks-lint](https://github.com/hyhmrright/brooks-lint) - AI code reviews grounded in six classic engineering books — decay risk diagnostics with book citations, severity labels, and four analysis modes (PR review, architecture audit, tech debt, test quality).
- [Claudable](https://github.com/opactorai/Claudable) - Claudable is an open-source web builder that leverages local CLI agents, such as Claude Code, Codex, Gemini CLI, Qwen Code, and Cursor Agent, to build and deploy products effortlessly.
- [claude-squad](https://github.com/smtg-ai/claude-squad) - Manage multiple AI terminal agents like Claude Code, Aider, Codex, OpenCode, and Amp.
- [async-code](https://github.com/ObservedObserver/async-code) - Use Claude Code / CodeX CLI to perform multiple tasks in parallel with a Codex-style UI. Your personal codex/cursor-background agent. 
- [cc-switch](https://github.com/farion1231/cc-switch) - A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Gemini CLI & Hermes Agent. Only official website: ccswitch.
- [codex-profiles](https://github.com/Ducksss/codex-profiles) - Switch Codex CLI and Desktop accounts with isolated CODEX_HOME profiles instead of copying auth files by hand.
- [ruler](https://github.com/intellectronica/ruler) - Ruler — apply the same rules to all coding agents
- [cc-sdd](https://github.com/gotalab/cc-sdd) - Spec-driven development (SDD) for your team's workflow. High quality commands that enforce structured requirements→design→tasks workflow and steering, transforming how you build with AI. Support Claude Code, Codex, Cursor, Github Copilot, Gemini CLI and Qwen Code.
- [vibekit](https://github.com/superagent-ai/vibekit) - Run Claude Code, Gemini, Codex — or any coding agent — in a clean, isolated sandbox with sensitive data redaction and observability baked in.
- [dotai](https://github.com/udecode/dotai) - Context Manager for Claude Code Plugins + Codex + Cursor.
- [zcf](https://github.com/UfoMiao/zcf) - Zero-config, one-click setup for Claude Code & Codex with bilingual support, intelligent agent system and personalized AI assistant
- [vsync](https://github.com/nicepkg/vsync) - Sync Skills, MCP servers, Agents & Commands across Claude Code, Cursor, OpenCode, and Codex with automatic format conversion (JSON ↔ TOML ↔ JSONC).
- [Bring Your AI](https://bringyour.ai/claude-code-to-codex) - Local-first Claude Code to Codex migration tool that keeps harness files local, maps AGENTS.md / CLAUDE.md guidance, MCP config, and skills, and records non-equivalent hooks as validation notes.
- [just-every/code](https://github.com/just-every/code) - fork of openai/codex focused on real developer ergonomics: Browser integration, multi-agents, theming, and reasoning control — all while staying compatible with upstream.
- [agnix](https://github.com/avifenesh/agnix) - Linter for AI agent configurations. Validates AGENTS.md, .codex/config.toml, skills, hooks, and MCP configs with 156 rules, auto-fix, and editor integration.
- [caliber](https://github.com/rely-ai-org/caliber) - CLI that fingerprints your codebase and generates AI agent configs (CLAUDE.md, .cursor/rules/, AGENTS.md, skills, MCPs) for Claude Code, Cursor, and Codex. Scores your setup 0–100.
- [bernstein](https://github.com/chernistry/bernstein) - Parallel multi-agent orchestrator — spawns Codex CLI, Claude Code, and Gemini CLI simultaneously on isolated git worktrees, verifies with tests, auto-commits working code. Zero LLM tokens on coordination.
- [ru-text](https://github.com/talkstream/ru-text) - Russian text quality — ~1,040 rules for typography, info-style, editorial, UX writing, business correspondence.
- [TokRepo](https://github.com/henu-wang/tokrepo) - Canonical GitHub landing page for the TokRepo open registry, with links to a Codex-compatible skill repo, MCP server, and installable AI assets such as prompts, workflows, and MCP configs.
- [trace-to-skill](https://github.com/grnbtqdbyx-create/trace-to-skill) - CLI for turning failed Codex, Claude Code, Cursor, and MCP-enabled agent runs into reusable AGENTS.md rules, SKILL.md files, eval evidence, PR comments, and SARIF code-scanning reports.
- [10000 Mentors Research Workflow](https://github.com/wd041216-bit/10000-mentors-research-workflow) - Codex-native autonomous research loop with source-gated mentor critique, submission-advisor reflection, bounded execution, and GitHub delivery.
- [SwarmVault](https://github.com/swarmclawai/swarmvault) - Local-first RAG knowledge base compiler. Turns raw docs, research, and code into a persistent markdown wiki, knowledge graph, and hybrid SQLite FTS + embeddings search. Ships a bundled skill and MCP server; works with Codex CLI, Claude Code, and OpenCode.
- [SwarmClaw](https://github.com/swarmclawai/swarmclaw) - Self-hosted multi-agent runtime that delegates to Codex CLI alongside Claude Code, Gemini CLI, OpenCode, Copilot CLI, Cursor Agent, Goose, Qwen Code, and Droid. Org chart view, schedules, runtime skills, persistent memory, and reviewed conversation-to-skill learning. MCP-native (server and client). Electron desktop app, CLI, and Docker.

### Stat
- [ccusage](https://github.com/ryoppippi/ccusage) - A CLI tool for analyzing Claude Code/Codex CLI usage from local JSONL files.
- [CodexBar](https://github.com/steipete/CodexBar) - Show usage stats for OpenAI Codex and Claude Code, without having to login.
- [agenttrace](https://github.com/luoyuctl/agenttrace) - Local TUI for inspecting AI coding-agent session logs, usage, cost, latency, tool failures, diffs, and CI gates.
- [WhereMyTokens](https://github.com/jeongwookie/WhereMyTokens) - Windows tray app for monitoring Claude Code and Codex token usage, costs, sessions, and rate limits from local JSONL logs.

#### Editor
- [zed](https://github.com/zed-industries/zed) - Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.

#### Termial
- [ghostty](https://github.com/ghostty-org/ghostty) - 👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.
- [Tmux](https://github.com/tmux/tmux) - tmux source code

#### System
- [omarchy](https://github.com/basecamp/omarchy) - Opinionated Arch/Hyprland Setup
 
## Official Resources

### Documentation
- [OpenAI Codex CLI Getting Started](https://help.openai.com/en/articles/11096431-openai-codex-cli-getting-started) - Official getting started guide
- [GitHub Repository](https://github.com/openai/codex) - Official OpenAI Codex CLI repository
- [OpenAI Codex Overview](https://openai.com/codex/) - Product overview and features

### Blog Posts & Tutorials
- [DataCamp Tutorial](https://www.datacamp.com/tutorial/open-ai-codex-cli-tutorial) - Comprehensive tutorial on using Codex CLI
- [Blott Studio Guide](https://www.blott.studio/blog/post/openai-codex-cli-build-faster-code-right-from-your-terminal) - Build faster code from your terminal
- [Medium Tutorial](https://medium.com/ai-software-engineer/how-to-install-and-use-openai-codex-cli-in-2-minutes-29e9fdd0e8c5) - Quick 2-minute setup guide
- [OpenReplay Integration Guide](https://blog.openreplay.com/integrate-openais-codex-cli-tool-development-workflow/) - How to integrate Codex CLI into your development workflow

## Web Interface Extensions

### Official Web Interface
- [Codex](https://chatgpt.com/codex) - Official cloud-based agent with web interface
- Cloud Codex - Sandbox environments preloaded with repositories (ChatGPT Pro/Enterprise/Team/Plus users)

### IDE Integrations
- **[Codex VS Code Extension](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)**: Codex is OpenAI's coding agent that helps you write, review, and ship code faster. Use it side-by-side in your IDE or delegate larger tasks to the cloud.
- **[Codexia VS Code Extension](https://github.com/milisp/codexia-vscode)**: A VS Code extension that provides a chat interface for the OpenAI Codex CLI, allowing you to interact with AI coding assistants directly from your editor.

## Use Cases

### Development Tasks
- **Refactoring**: Modernize legacy code and improve structure.
- **Testing**: Generate comprehensive test suites.
- **Bug Fixes**: Identify and resolve issues quickly.
- **Documentation**: Generate and maintain code documentation.
- **Feature Development**: Scaffold new features and components.

### Specialized Tasks
- **Frontend Development**: React components, CSS generation, responsive designs.
- **Data Analysis**: Dataset exploration, Python scripting, ML projects.
- **Code Understanding**: Legacy code analysis and architecture insights.

---

## Community

### Discussions
- [Hacker News Discussion](https://news.ycombinator.com/item?id=43708025) - Community reactions and experiences
- [Machine Learning Mastery](https://machinelearningmastery.com/understanding-openai-codex-cli-commands/) - Understanding CLI commands

### Learning Resources
- [Apidog Blog](https://apidog.com/blog/openai-codex-cli/) - Open source coding agent overview
- Community tutorials and examples (contribute yours!)

### Community Projects
- **[Plux](https://github.com/milisp/plux)** - AI finder/explorer with visual file tree.
- **[awesome-claude-dxt](https://github.com/milisp/awesome-claude-dxt)** - Curated list of Claude Desktop Extensions.
- **[awesome-gpt-oss](https://github.com/milisp/awesome-gpt-oss)** - Curated GPT open-source resources.
- **[awesome-chatgpt-claude-agents](https://github.com/milisp/awesome-chatgpt-claude-agents)** - Collection of awesome agents and AI development tools.

---

## Contributing

Contributions are welcome! Please:
1. Read the [contribution guidelines](contributing.md).
2. Check existing resources to avoid duplicates.
3. Ensure links are working and relevant.
4. Submit a pull request with clear descriptions.

## Growing thanks to you
[![Stargazers over time](https://starchart.cc/milisp/awesome-codex-cli.svg?variant=adaptive)](https://starchart.cc/milisp/awesome-codex-cli)

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work.
