# Awesome Codex CLI 🚀 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Stars](https://img.shields.io/github/stars/milisp/awesome-codex-cli?style=social)](https://github.com/milisp/awesome-codex-cli)
[![Follow on 𝕏](https://img.shields.io/badge/𝕏-@lisp__mi-1c9bf0)](https://x.com/lisp_mi)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/codex?style=flat&logo=reddit&label=subreddit)](https://reddit.com/r/codex)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/zAjtD4kf5K)

> A curated list of tools, plugins, skills, resources, and tutorials for OpenAI Codex CLI — hand-picked and reviewed, not auto-collected.

---

> 💡 **[Follow me on 𝕏](https://x.com/lisp_mi)** for agentic workflows, building in public

### ✨ Featured Tools

> Maintainer picks, including my own projects.

- **[keke](https://github.com/milisp/keke-agent)** - Lightweight Rust coding agent harness. BYOK, 8 MB.
- **[Plux](https://milisp.dev/plux)** - Capture now with a shortcut. Turn it into a todo, send it to (Codex / ChatGPT / Claude) anytime.
- **[productship.lol](https://productship.lol)** - Discover and showcase AI tools.

---

## Contents

- [What is OpenAI Codex CLI](#what-is-openai-codex-cli)
- [Tools](#tools)
  - [GUI & Apps](#gui-apps)
  - [Mobile & Remote Access](#mobile--remote-access)
  - [Session Managers](#session-managers)
  - [Agent Runtimes & Orchestration](#agent-runtimes--orchestration)
  - [Sandboxes](#sandboxes)
  - [Account Switchers & Proxies](#account-switchers--proxies)
  - [Usage & Monitoring](#usage--monitoring)
  - [Setup & Config Management](#setup--config-management)
  - [Forks & Patched Builds](#forks--patched-builds)
  - [Code Quality & Review](#code-quality--review)
  - [Claude Code Interop](#claude-code-interop)
  - [Terminal](#terminal)
- [Customize](#customize)
  - [Plugins](#plugins)
  - [Agent Skills](#agent-skills)
    - [General](#general)
    - [Domain-Specific](#domain-specific)
  - [MCP Servers](#mcp-servers)
    - [Management](#management)
    - [Memory & Context](#memory--context)
    - [Utilities](#utilities)
  - [Directories & Registries](#directories--registries)
- [Workflows & Knowledge Guides 🧠](#workflows--knowledge-guides-)
- [Resources](#resources)
  - [Documentation](#documentation)
  - [Blog Posts & Tutorials](#blog-posts--tutorials)
- [Web Interface Extensions](#web-interface-extensions)
  - [Official Web Interface](#official-web-interface)
  - [IDE Integrations](#ide-integrations)
- [Use Cases](#use-cases)
  - [Development Tasks](#development-tasks)
  - [Specialized Tasks](#specialized-tasks)
- [Community](#community)
  - [Discussions](#discussions)
  - [Learning Resources](#learning-resources)
  - [Community Projects](#community-projects)

## What is OpenAI Codex CLI

OpenAI Codex CLI is a lightweight coding agent that runs in your terminal.

## Tools

### GUI & Apps

- [Codexia](https://github.com/milisp/codexia) - Agent Workstation for Codex CLI and claude code
- [CodexMonitor](https://github.com/Dimillian/CodexMonitor) - An app to monitor the Codex situation.
- [CodexFlow](https://github.com/lulu-sk/CodexFlow) - An enhanced GUI tool designed for Codex CLI, focused on improving conversation management and interaction.
- [AionUi](https://github.com/iOfficeAI/AionUi) - Open-source desktop client that runs Codex CLI alongside other agent CLIs (Claude Code, Gemini CLI, Qwen Code), with multi-session chat, MCP and ACP support, and local file management.
- [Claudable](https://github.com/anymorph-ai/Claudable) - An open-source web builder that leverages local CLI agents, such as Claude Code, Codex, Gemini CLI, Qwen Code, and Cursor Agent, to build and deploy products effortlessly.

### Mobile & Remote Access

- [happy](https://github.com/slopus/happy) - Mobile and Web client for Codex and Claude Code, with real-time voice and encryption.
- [Untether](https://github.com/littlebearapps/untether) - Telegram bridge for Codex CLI (and 5 other agents). Send tasks by voice, stream progress, toggle approval policy (full auto/safe) via inline buttons.
- [Codex on Telegram](https://github.com/leoshenzh/codex-on-telegram) - Self-hosted macOS bridge that drives your local Codex CLI (or Claude Code) sessions from Telegram. Attach to a session already running on your machine, approve permission prompts in chat, run per-topic parallel sessions, and resume the same session after a restart.
- [IM.codes](https://github.com/im4codes/imcodes) - The IM for agents: a mobile/web control layer for Codex CLI and other terminal-based coding agents, with terminal access, file browsing, Git views, localhost preview, notifications, and multi-agent workflows.
- [Onepilot](https://onepilotapp.com) - Native iOS SSH terminal for Codex CLI and Claude Code. Full PTY, GitHub integration, localhost forwarding, live file editing, and one-click AI agent deployment via OpenClaw.
- [Redock](https://redock.dev) - Native Android & iOS SSH/Mosh terminal for running Codex CLI on your own host, with tmux session continuity, project shortcuts, reusable actions, and voice input. [App Store](https://apps.apple.com/app/id6763979847) [Google Play](https://play.google.com/store/apps/details?id=com.redock.android).
- [Mobile SSH](https://mobile-ssh.github.io/) - Android & iOS SSH/SFTP terminal for running Codex and Claude Code on a remote server. Agent Alerts push a phone notification (sound + vibration) the moment the agent needs input, plus a multi-server tmux session manager, Eternal Terminal transport, and multi-address LAN/VPN roaming.
- [MulmoTerminal](https://github.com/receptron/mulmoterminal) - Browser grid of live Claude Code / Codex sessions started with one `npx` command. Each cell is a real PTY with a colour-coded status, tmux-backed persistence, and a git worktree per cell. For Claude Code, needs-you is shown separately from done, read from the CLI's own hooks.

### Session Managers

- [crystal](https://github.com/stravu/crystal) - Run multiple Codex and Claude Code AI sessions in parallel Git worktrees. Test, compare approaches & manage AI-assisted development workflows in one desktop app.
- [Parallel Code](https://github.com/johannesjo/parallel-code) - Desktop app for running Codex CLI, Claude Code, and Gemini CLI agents side by side in separate Git worktrees.
- [Orca](https://www.onorca.dev/) - Desktop IDE that runs Codex CLI and other agents (Claude Code, Cursor, Gemini) in parallel, each in its own Git worktree, with built-in terminal and diff review.
- [vibe-kanban](https://github.com/BloopAI/vibe-kanban) - Kanban board to manage your AI coding agents.
- [ccmanager](https://github.com/kbwo/ccmanager) - Coding Agent Session Manager that supports Claude Code / Gemini CLI / Codex CLI / Cursor Agent / Copilot CLI.
- [claude-squad](https://github.com/smtg-ai/claude-squad) - Manage multiple AI terminal agents like Claude Code, Aider, Codex, OpenCode, and Amp.
- [async-code](https://github.com/ObservedObserver/async-code) - Use Claude Code / CodeX CLI to perform multiple tasks in parallel with a Codex-style UI. Your personal codex/cursor-background agent. 
- [codmate](https://github.com/loocor/codmate) - A macOS SwiftUI app for managing CLI AI sessions.
- [agent-sessions](https://github.com/jazzyalex/agent-sessions) - Local-first macOS app for browsing and full-text searching Codex session history alongside other local coding-agent transcripts; resume is available where the underlying CLI supports it.
- [cctop](https://github.com/st0012/cctop) - Keyboard-first macOS menubar monitor for Codex CLI sessions. Shows which runs are working, waiting, or need approval, jumps back to the exact terminal pane, and also supports Codex Desktop, Claude Code, opencode, and pi.
- [GraphCode](https://github.com/scgopi/GraphCode) - macOS app that arranges Codex, Claude Code, and Copilot CLI sessions into a graph. Each node is a live terminal you can attach to mid-run; each edge is a hand-off, message, or spawn that fires while you're away. Sessions survive app quits and reboots.
- [agent-manager](https://github.com/YoanWai/agent-manager) - Terminal UI that runs Codex CLI and other coding-agent CLIs side by side, each in its own persistent tmux session, with live status, prompts sent without attaching, optional per-session Git worktrees, and a diff review that sends line comments back to the agent.

### Agent Runtimes & Orchestration

- [humanlayer](https://github.com/humanlayer/humanlayer) - The best way to get AI coding agents to solve hard problems in complex codebases.
- [bernstein](https://github.com/sipyourdrink-ltd/bernstein) - Parallel multi-agent orchestrator — spawns Codex CLI, Claude Code, and Gemini CLI simultaneously on isolated Git worktrees, verifies with tests, auto-commits working code. Zero LLM tokens on coordination.
- [YYLO](https://github.com/yylo-dev/yylo) - Command-line orchestrator for coding agents with typed task, validation, merge, and release-readiness boundaries. Runs Pi and Codex subagents, gives each task a dedicated branch/worktree, and gates merges with a risk-based review queue and receipt-backed changes. MIT, npm @yylo/cli.
- [Ordewell](https://github.com/ordewell/ordewell) - Terminal CLI and TUI that turns one goal into an ordered, editable plan of coding agent tasks, each with its own runner (Codex, Claude Code, OpenCode), model and mode.
- [Claudexor](https://github.com/razzant/claudexor) - Local-first control plane that runs Codex alongside Claude Code, Cursor, and OpenCode, with profile-aware quota routing, best-of-N runs, and cross-family review.
- [SwarmClaw](https://github.com/swarmclawai/swarmclaw) - Self-hosted multi-agent runtime that delegates to Codex CLI alongside Claude Code, Gemini CLI, OpenCode, Copilot CLI, Cursor Agent, Goose, Qwen Code, and Droid. Org chart view, schedules, runtime skills, persistent memory, and reviewed conversation-to-skill learning. MCP-native (server and client). Electron desktop app, CLI, and Docker.
- [Agentlas OS](https://github.com/agentlas-ai/Agentlas-OS) - Local-first Agent OS that packages specialist agents and temporary teams, with a Codex adapter, MCP/A2A routing, and verification gates.
- [Aeon](https://github.com/aeonfun/aeon) - Autonomous agent framework that runs entirely inside GitHub Actions — cron-scheduled Markdown skills, self-healing (a health skill files issues, a repair skill fixes them by PR), and fleet-replicating. Runs its skills on Codex CLI, one of six supported coding-agent harnesses (Codex, Claude Code, Grok, Pi, Vibe, Kimi), through a single adapter. MIT.
- [Ouroboros](https://github.com/Q00/ouroboros) - Agent OS for repeatable AI coding workflows. It turns vague goals into executable Seeds through an interview, then runs staged, budgeted evaluation loops with Codex CLI or 12 other runtimes.
- [Ouroboros (razzant)](https://github.com/razzant/ouroboros) - Self-hosted AI agent runtime with a headless CLI, persistent memory, reviewed self-modification, and Codex CLI integration.

### Sandboxes

- [agentbox](https://github.com/madarco/agentbox) - Run multiple Codex (and Claude Code / OpenCode) sessions in parallel, each in its own sandboxed box — local Docker or cloud VMs (Hetzner/Daytona/Vercel/E2B). Sub-1s checkpoint starts, per-box browser + VS Code, and a dashboard to switch between boxes.
- [vibekit](https://github.com/superagent-ai/vibekit) - Run Claude Code, Gemini, Codex — or any coding agent — in a clean, isolated sandbox with sensitive data redaction and observability baked in.
- [codex-universal](https://github.com/openai/codex-universal) - Base Docker image used in Codex environments.

### Account Switchers & Proxies

- [codex-account](https://github.com/frndchagas/codex-account) - Switch between multiple Codex accounts without signing out — never revokes tokens, keeps every account signed in, and syncs refreshed tokens back into saved profiles. Single-file bash script.
- [Codex Account Switcher](https://github.com/liuzhao1225/codex-account-switcher) - Native macOS menu bar app that switches the active Codex Desktop and newly started Codex CLI account locally, with no Terminal commands or config-file editing.
- [codex-profiles](https://github.com/Ducksss/codex-profiles) - Switch Codex CLI and Desktop accounts with isolated CODEX_HOME profiles instead of copying auth files by hand.
- [cc-switch](https://github.com/farion1231/cc-switch) - A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Gemini CLI & Hermes Agent. Only official website: ccswitch.
- [opencodex](https://github.com/lidge-jun/opencodex) - Universal provider proxy for Codex — use Claude, Gemini, Grok, GLM, DeepSeek, Kimi, Cursor, and more with the Codex CLI/App/SDK, with multi-account pooling and a GUI dashboard.
- [aisw](https://github.com/burakdede/aisw) - Rust CLI that keeps each Codex CLI login in its own `CODEX_HOME` profile and switches accounts in one command, alongside Claude Code, Gemini CLI and Antigravity CLI, with per-repository account guards. Docs: [aiswitcher.dev](https://aiswitcher.dev).

### Usage & Monitoring

- [ccusage](https://github.com/ccusage/ccusage) - A CLI tool for analyzing Claude Code/Codex CLI usage from local JSONL files.
- [ax](https://github.com/Necmttn/ax) - Local-first telemetry and memory graph for Codex CLI, Claude Code, OpenCode, Cursor, and Pi histories with cost analytics, skill/hook usage, workflow extraction, dashboard, and MCP access.
- [CodexBar](https://github.com/steipete/CodexBar) - Show usage stats for OpenAI Codex and Claude Code, without having to login.
- [agenttrace](https://github.com/luoyuctl/agenttrace) - Local TUI for inspecting AI coding-agent session logs, usage, cost, latency, tool failures, diffs, and CI gates.
- [WhereMyTokens](https://github.com/jeongwookie/WhereMyTokens) - Windows tray app for monitoring Claude Code and Codex token usage, costs, sessions, and rate limits from local JSONL logs.
- [ClawMetry](https://github.com/vivekchand/clawmetry) - Zero-config local dashboard for observing Codex CLI sessions, tokens, and costs alongside 20+ other agent runtimes.
- [session-top](https://github.com/jerryxff26-alt/session-top) - Local htop-style TUI for Codex CLI sessions: quota windows, top consumers, and explainable usage drops from on-disk rollouts.
- [Agent Island](https://github.com/tristan666666/agent-island) - Free, MIT-licensed native companion for Codex, Claude Code, Antigravity, Grok and Cursor: local working/stalled/your-turn state, your-turn alerts, and provider usage with on-device cost estimates. macOS and Windows, no account, no telemetry.
- [Crest](https://crestnotch.app/claude-code-notch) - macOS notch app that shows Codex and Claude Code permission requests in the MacBook notch, where Allow, Deny or one of the prompt's options is a single tap and the answer goes back into the session, through each CLI's own hooks. Free tier; the AI Coding module is part of Crest Pro, $19.99 once.
- [EchoCoding](https://github.com/launsion-boop/EchoCoding) - Audio layer for Codex CLI with hook-triggered SFX, ambient soundscape, and optional cloud TTS/ASR voice interaction.
- [Relay Baton](https://github.com/guorunjie/codex-relay-baton-guardian) - Local Codex Desktop/CLI recovery monitor for long-running tasks. Detects compact failures and context-window overflow, then queues audited handoff bundles.

#### Rate limit Tracks
- [WhenResets](https://whenresets.net) - Sourced public ledger of every OpenAI Codex rate-limit reset: 55 records, each linking to the original announcement. Also published as MIT-licensed CSV/JSON.

### Setup & Config Management

- [codex-1up](https://github.com/regenrek/codex-1up) - Equips your Codex CLI coding agent with powerful tools.
- [zcf](https://github.com/UfoMiao/zcf) - Zero-config, one-click setup for Claude Code & Codex with bilingual support, intelligent agent system and personalized AI assistant.
- [ruler](https://github.com/intellectronica/ruler) - Applies the same rules to all coding agents.
- [dotai](https://github.com/udecode/dotai) - Context Manager for Claude Code Plugins + Codex + Cursor.
- [vsync](https://github.com/nicepkg/vsync) - Sync Skills, MCP servers, Agents & Commands across Claude Code, Cursor, OpenCode, and Codex with automatic format conversion (JSON ↔ TOML ↔ JSONC).
- [Bring Your AI](https://bringyour.ai/claude-code-to-codex) - Local-first Claude Code to Codex migration tool that keeps harness files local, maps AGENTS.md / CLAUDE.md guidance, MCP config, and skills, and records non-equivalent hooks as validation notes.
- [agnix](https://github.com/agent-sh/agnix) - Linter for AI agent configurations. Validates AGENTS.md, .codex/config.toml, skills, hooks, and MCP configs with 156 rules, auto-fix, and editor integration.
- [caliber](https://github.com/caliber-ai-org/ai-setup) - CLI that fingerprints your codebase and generates AI agent configs (CLAUDE.md, .cursor/rules/, AGENTS.md, skills, MCPs) for Claude Code, Cursor, and Codex. Scores your setup 0–100.
- [Codex Skins](https://www.codexskins.org/) - One-click wallpaper/theme gallery for the OpenAI Codex desktop app. Reversible full-window CDP theme injection, macOS/Windows. Open-source engine (MIT).

### Forks & Patched Builds

- [just-every/code](https://github.com/just-every/code) - A fork of OpenAI Codex focused on real developer ergonomics: Browser integration, multi-agents, theming, and reasoning control — all while staying compatible with upstream.
- [codex-patch-overlay](https://github.com/salty-flower/codex-patch-overlay) - Patched Codex CLI builds carrying community-requested features upstream hasn't merged (live TUI reasoning streaming, completion sound, WebP image input). Ships ready-to-run macOS/Linux binaries plus a Nix overlay, refreshed each upstream release.

### Code Quality & Review

- [brooks-lint](https://github.com/hyhmrright/brooks-lint) - AI code reviews grounded in six classic engineering books — decay risk diagnostics with book citations, severity labels, and four analysis modes (PR review, architecture audit, tech debt, test quality).
- [unslop](https://github.com/MohamedAbdallah-14/unslop) - CLI and MCP server that removes AI writing patterns from agent-generated text. Works with Codex, Claude Code, Gemini CLI, and Cursor. Five intensity levels and lint-only audit mode.

### Claude Code Interop

- [claude-codex-bridge](https://github.com/jackcongmac/claude-codex-bridge) - Bidirectional MCP bridge for Codex CLI and Claude Code collaboration, with persistent Claude sessions and shared collaboration files.
- [Codex Skill](https://github.com/skills-directory/skill-codex) by [klaudworks](https://github.com/klaudworks) - Enables users to prompt codex from claude code. Unlike the raw codex mcp server, this skill infers parameters such as model, reasoning effort, sandboxing from your prompt or asks you to specify them. It also simplifies continuing prior codex sessions so that codex can continue with the prior context.
- [great_cto](https://github.com/avelikiy/great_cto) - Ships nine skills and an MCP server to Codex CLI, and runs Codex as a second-opinion reviewer on the same diff from inside Claude Code.

### Terminal

- [ghostty](https://github.com/ghostty-org/ghostty) - 👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.
- [Tmux](https://github.com/tmux/tmux) - Source code for the terminal multiplexer.

## Customize

### Plugins

> Plugins bundle skills, MCP servers and other resources that Codex CLI installs from a marketplace with `codex plugin add`.

- [Supercov](https://github.com/supercorp-ai/supercov) by [Supercorp](https://github.com/supercorp-ai) - Codex plugin with two skills: one runs the project's existing tests, measures line, branch and MC/DC coverage and writes tests for the untested code, the other scans source for security vulnerabilities.
- [Claude Codex Settings](https://github.com/fcakyon/claude-codex-settings) by [fatih akyon](https://github.com/fcakyon) - A well-organized, well-written set of plugins covering core developer activities, such as working with common cloud platforms like GitHub, Azure, MongoDB, and popular services such as Tavily, Playwright, and more. Clear, not overly-opinionated, and compatible with a few other providers.
- [Compound Engineering Plugin](https://github.com/EveryInc/compound-engineering-plugin) by [EveryInc](https://github.com/EveryInc) - A very pragmatic set of well-designed agents, skills, and commands, built around a discipline of turning past mistakes and errors into lessons and opportunities for future growth and improvement. Good documentation.

### Agent Skills

> Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Codex CLI to perform specialized tasks requiring specific knowledge or capabilities.

#### General

- [Codex Skills](https://github.com/openai/skills) - A catalog of reusable skills for Codex.
- [Codex Skills](https://github.com/Dimillian/Skills) - A skill collection maintained by Dimillian.
- [gstack](https://github.com/garrytan/gstack) - A 23-skill suite covering planning, design review, shipping, canary, QA, and retros. Installs to `~/.codex/skills/` via `--host codex`; the `/codex` skill runs Codex CLI as an adversarial second-opinion reviewer against Claude's findings.
- [Everything OpenAI Codex](https://github.com/mturac/everything-openai-codex) by [Mehmet Turac](https://github.com/mturac) - Open-source Codex workflow system with agents, skills, commands, hooks, memory patterns, install profiles, and validation checks for repeatable coding sessions.
- [Context Engineering Kit](https://github.com/NeoLabHQ/context-engineering-kit) by [Vlad Goncharov](https://github.com/LeoVS09) - Hand-crafted collection of advanced context engineering techniques and patterns with minimal token footprint focused on improving agent result quality.
- [AgentSys](https://github.com/agent-sh/agentsys) by [avifenesh](https://github.com/avifenesh) - Workflow automation system for Claude with a group of useful plugins, agents, and skills. Automates task-to-production workflows, PR management, code cleanup, performance investigation, drift detection, and multi-agent code review. Includes [agnix](https://github.com/agent-sh/agnix) for linting agent configurations. Built on thousands of lines of code with thousands of tests. Uses deterministic detection (regex, AST) with LLM judgment for efficiency. Used on many production systems.
- [These are the rules](https://x.com/kevinkern/status/1965113557160484961) to make code search faster and more accurate. - [Kevin Kern](https://bsky.app/profile/kevinkern.dev)

#### Domain-Specific

- [cc-devops-skills](https://github.com/akin-ozer/cc-devops-skills) by [akin-ozer](https://github.com/akin-ozer) - A practical agent skill pack for DevOps work in Claude Code and Codex.
- [Trail of Bits Security Skills](https://github.com/trailofbits/skills) by [Trail of Bits](https://github.com/trailofbits) - A very professional collection of over a dozen security-focused skills for code auditing and vulnerability detection. Includes skills for static analysis with CodeQL and Semgrep, variant analysis across codebases, fix verification, and differential code review.
- [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) by [K-Dense](https://github.com/K-Dense-AI/) - "A set of ready-to-use Agent Skills for research, science, engineering, analysis, finance and writing." That's their description - modest, simple. That's how you can tell this is really one of the best skills repos on GitHub. If you've ever thought about getting a PhD... just read all of these documents instead. Also I think it IS an AI agent or something? Awesome.
- [harmony-next.skills](https://github.com/linhay/harmony-next.skills) by [linhay](https://github.com/linhay) - HarmonyOS NEXT developer skill for Codex and other coding agents, with local ArkTS/ArkUI/API references, DevEco Studio workflows, Emulator/HDC automation, UI/UX audit, trace audit, and Empty Ability smoke-test templates.
- [NotFair](https://github.com/nowork-studio/notfair-plugin) by [nowork-studio](https://github.com/nowork-studio) - Seventeen host-agnostic SKILL.md workflows for SEO, GEO, Google Ads, and Meta Ads, plus an open-source local goal agent that supports Codex.
- [Codex Small Business Skills](https://github.com/simongonzalezdc/codex-small-business-skills) by [Simon Gonzalez De Cruz](https://github.com/simongonzalezdc) - Apache-2.0 Codex port of Anthropic's Small Business skills, with 31 workflows for cash flow, invoices, CRM, support, marketing, hiring, and weekly business rhythm.
- [assay](https://github.com/awss1i/assay) by [awss1i](https://github.com/awss1i) - Deterministic web-page QA skill. After the agent changes a page, it opens the page in Chromium through Playwright, drives every control, and reports where the page contradicts itself. No tests to write, no LLM. Install with pip install assay-ui.

### MCP Servers

#### Management

- [MCP Linker](https://github.com/milisp/mcp-linker) - GUI for managing MCP configs for Codex CLI.

#### Memory & Context

- [GBrain](https://github.com/garrytan/gbrain) - Persistent brain layer for Codex CLI: synthesis, graph traversal, and gap analysis over your own corpus, so the agent stops being amnesiac about everything that is not code. `codex plugin marketplace add garrytan/gbrain@codex-plugin`; PGLite, no server.
- [Vestige](https://github.com/samvallad33/vestige) - Local-first cognitive memory MCP server that gives Codex CLI persistent recall across sessions. SQLite storage, FSRS-6 retention with active forgetting so old context decays instead of piling up, prediction-error gating, and hybrid retrieval. Single Rust binary, npm install -g vestige-mcp-server.
- [GoodMemory](https://github.com/hjqcan/GoodMemory) - Local-first, auditable memory for Codex CLI and Claude Code. `goodmemory setup` installs scoped recall hooks and read-only MCP inspection; SQLite persistence is the default, while optional writeback stays reviewable and reversible.
- [Selvedge](https://github.com/masondelan/selvedge) - Local SQLite decision memory for Codex CLI via stdio MCP, storing explicit decisions, reasons, and rejected approaches for retrieval across sessions.
- [AccInt](https://github.com/maxbaluev/accreted-intelligence) - Local-first MCP work memory for Codex CLI, Claude Code, OpenCode, and Cursor with scored retrieval, commitment tracking, and outcome-based credit across sessions.
- [Tree Ring Memory](https://terminallylazy.github.io/Tree-Ring-Memory/) - Local-first memory lifecycle layer for AI agents with Rust CLI, SQLite/FTS recall, audit, forgetting, consolidation, and terminal TUI.
- [SwarmVault](https://github.com/swarmclawai/swarmvault) - Local-first RAG knowledge base compiler. Turns raw docs, research, and code into a persistent markdown wiki, knowledge graph, and hybrid SQLite FTS + embeddings search. Ships a bundled skill and MCP server; works with Codex CLI, Claude Code, and OpenCode.
- [ContextStream](https://contextstream.io) - Remote MCP server for shared project context across Codex CLI, Claude Code, Cursor, and Grok. Endpoint: https://mcp.contextstream.io/mcp. Repo: https://github.com/contextstream/mcp-server.
- [OrcaReplay](https://github.com/Continuum-AI-Corp/OrcaReplay) - Records a Codex CLI session below the harness and replays it with the recorded model responses served back; `orca mcp` exposes the recorded runs so an agent can read what an earlier run sent, ran and changed.

#### Utilities

- [prompt-to-asset](https://github.com/MohamedAbdallah-14/prompt-to-asset) - MCP server that generates app icons, favicons, OG images, logos, and wordmarks by routing requests across 30+ image generation models. Zero API key needed on first run via free-tier providers.
- [click-to-mcp](https://github.com/Coding-Dev-Tools/click-to-mcp) - Auto-wrap any Python Click/Typer CLI as an MCP server. Zero-code transformation that introspects CLI commands and exposes them as MCP tools. Works with Codex CLI, Claude Code, and any MCP client. `pip install click-to-mcp`
- [Agent QA](https://github.com/vostride/agent-qa) - The self-improving QA agent for software teams. Run `agent-qa mcp` to let Codex author and execute natural-language web/mobile tests, inspect artifacts, triage failures, and guide fixes with persistent test memory.
- [VideoOverlayKit](https://github.com/alichherawalla/video-overlay-kit) - MCP server that renders 4-6s animated b-roll overlay videos (mp4) for short-form social (LinkedIn, IG Reels, YouTube Shorts, TikTok). Paste your script into Codex CLI / Claude Code / Cursor, the model writes the scene spec and renders the mp4. Built on Remotion + Tabler + Lottie. Free, MIT, local.
- [x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper) - X/Twitter data extraction skill & MCP server for AI coding agents. 20 tools: followers, tweets, replies, mentions, lists, hashtags, spaces & more.
- [REA](https://github.com/morluto/rea) - Local CLI and MCP server for agent-assisted reverse engineering of native binaries, JavaScript/Electron apps, and .NET assemblies, with evidence provenance; native deep analysis needs separately installed Hopper, Ghidra, or IDA.
- [Tapetide MCP](https://github.com/Tapetide-hq/nse-bse-indian-stock-market-data-mcp) - Indian stock market data for Codex CLI: quotes, financials, shareholding, a 326-ratio screener, FII/DII flows and option chains for about 8,200 NSE and BSE stocks. `npx -y tapetide-mcp` with a free token, or remote at `https://mcp.tapetide.com/mcp`.

### Directories & Registries

- [TokRepo](https://github.com/henu-wang/tokrepo) - Canonical GitHub landing page for the TokRepo open registry, with links to a Codex-compatible skill repo, MCP server, and installable AI assets such as prompts, workflows, and MCP configs.
- [Agent Plugins Directory](https://agentpluginsdirectory.com) - Directory of 524 Agent Plugins, each verified by fetching its `plugin.json` and checking it against the official Agent Plugins 1.0.0 schema, plus a free browser-based validator for `plugin.json` and `mcp.json`. Agent Plugins install in Codex CLI and in ChatGPT, Cursor, Copilot, VS Code and Kiro from the same directory.
- [Hexis](https://github.com/Bevel-Software/Hexis) - Git-backed platform for skills, tools, and context for AI agents, available to Codex through a remote OAuth MCP server.

## Workflows & Knowledge Guides 🧠

> A workflow is a tightly coupled set of Codex-native resources that facilitate specific projects

- [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) - OmX - Oh My codeX: Your codex is not alone. Add hooks, agent teams, HUDs, and so much more.
- [ralph-harness](https://github.com/rxdt/loopgate_harness) - Minimal repo-local loop scaffold for Codex CLI, Claude Code, and Gemini CLI. Uses `PROMPT.md`, specs, fresh-context iterations, Git hooks, CI verification, and hard iteration/time caps so agents make small gated commits instead of drifting in one long chat.
- [cc-sdd](https://github.com/gotalab/cc-sdd) - Spec-driven development (SDD) for your team's workflow. High quality commands that enforce structured requirements→design→tasks workflow and steering, transforming how you build with AI. Support Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI and Qwen Code.
- [Archcore](https://github.com/archcore-ai/archcore) - Spec-driven development and context engineering for Claude Code, Cursor, Codex, and GitHub Copilot — backed by project context in Git.
- [10000 Mentors Research Workflow](https://github.com/wd041216-bit/10000-mentors-research-workflow) - Codex-native autonomous research loop with source-gated mentor critique, submission-advisor reflection, bounded execution, and GitHub delivery.
- [trace-to-skill](https://github.com/grnbtqdbyx-create/trace-to-skill) - CLI for turning failed Codex, Claude Code, Cursor, and MCP-enabled agent runs into reusable AGENTS.md rules, SKILL.md files, eval evidence, PR comments, and SARIF code-scanning reports.
- [Codex First Task Prompt Generator](https://ronnie2025.github.io/ai-agent-workbench-starter-pack/codex-first-task-prompt-generator.html) - Free web tool that turns a Codex CLI project goal into a scoped first-task prompt with constraints and acceptance checks.

## Resources

### Documentation

- [OpenAI Codex CLI Getting Started](https://help.openai.com/en/articles/11096431-openai-codex-cli-getting-started) - Official getting started guide.
- [GitHub Repository](https://github.com/openai/codex) - Official OpenAI Codex CLI repository.
- [OpenAI Codex Overview](https://openai.com/codex/) - Product overview and features.
- [Agents.md](https://agents.md) - A simple, open format for guiding coding agents, used by over 20k open-source projects.

### Blog Posts & Tutorials

- [DataCamp Tutorial](https://www.datacamp.com/tutorial/open-ai-codex-cli-tutorial) - Comprehensive tutorial on using Codex CLI.
- [Blott Studio Guide](https://www.blott.com/blog/post/openai-codex-cli-build-faster-code-right-from-your-terminal) - Build faster code from your terminal.
- [Medium Tutorial](https://medium.com/ai-software-engineer/how-to-install-and-use-openai-codex-cli-in-2-minutes-29e9fdd0e8c5) - Quick 2-minute setup guide.
- [OpenReplay Integration Guide](https://blog.openreplay.com/integrate-openais-codex-cli-tool-development-workflow/) - How to integrate Codex CLI into your development workflow.

## Web Interface Extensions

### Official Web Interface

- [Codex](https://chatgpt.com/codex) - Official cloud-based agent with web interface.
- Cloud Codex - Sandbox environments preloaded with repositories (ChatGPT Pro/Enterprise/Team/Plus users)

### IDE Integrations

- [Codex VS Code Extension](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt) - Codex is OpenAI's coding agent that helps you write, review, and ship code faster. Use it side-by-side in your IDE or delegate larger tasks to the cloud.
- [zed](https://github.com/zed-industries/zed) - Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.

## Use Cases

### Development Tasks

Common development tasks include refactoring legacy code, generating test suites,
fixing bugs, maintaining documentation, and scaffolding features.

### Specialized Tasks

Specialized tasks include frontend development, data analysis, and understanding
legacy code and architecture.

---

## Community

### Discussions

- [Hacker News Discussion](https://news.ycombinator.com/item?id=43708025) - Community reactions and experiences.
- [Machine Learning Mastery](https://machinelearningmastery.com/understanding-openai-codex-cli-commands/) - Understanding CLI commands.

### Learning Resources

- [Apidog Blog](https://apidog.com/blog/openai-codex-cli/) - Open source coding agent overview.
- [AGENTS.md Practical Guide (Korean)](https://github.com/soul-sol/agents-md-guide-ko) by [soul-sol](https://github.com/soul-sol) - Korean guide to Codex instruction discovery, nested overrides, repository boundaries, completion criteria, and ready-to-use single-service, monorepo, and library examples.

Community tutorials and examples are welcome.

### Community Projects

- [awesome-claude-dxt](https://github.com/milisp/awesome-claude-dxt) - Curated list of Claude Desktop Extensions.
- [awesome-gpt-oss](https://github.com/milisp/awesome-gpt-oss) - Curated GPT open-source resources.
- [awesome-chatgpt-claude-agents](https://github.com/milisp/awesome-chatgpt-claude-agents) - Collection of awesome agents and AI development tools.

---

## Contributing

Contributions are welcome! Please:

1. Read the [contribution guidelines](contributing.md).
2. Check existing resources to avoid duplicates.
3. Ensure links are working and relevant.
4. Submit a pull request with clear descriptions.
