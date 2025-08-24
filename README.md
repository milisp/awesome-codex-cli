<div align="center">

![icon](icon.png)

# Awesome Codex CLI 🚀

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Stars](https://img.shields.io/github/stars/milisp/awesome-codex-cli?style=social)](https://github.com/milisp/awesome-codex-cli/stargazers)

A curated list of awesome resources, tools, and tutorials for OpenAI Codex CLI - the lightweight coding agent that runs in your terminal.

  [Codex CLI](https://github.com/openai/codex) |
  [Codex Web](https://chatgpt.com/codex) |
  [Codexia GUI](https://github.com/milisp/codexia)
</div>

## What is OpenAI Codex CLI?

OpenAI Codex CLI is an open-source command-line tool that brings the power of OpenAI's latest reasoning models directly to your terminal. It acts as a lightweight coding agent that can read, modify, and run code on your local machine to help you build features faster, squash bugs, and understand unfamiliar code.

## Key Features

- **🔒 Privacy First**: Your source code never leaves your environment - all operations happen locally
- **⚡ Zero Setup**: Single command installation with `npm install -g @openai/codex`
- **🖼️ Multimodal**: Support for text, screenshots, and diagrams as inputs
- **🤖 Model Flexibility**: Supports GPT-5, o3, o4-mini, and third-party models
- **🌍 Cross-Platform**: Official support for macOS and Linux (Windows via WSL)

## Installation & Setup

<details>

### Quick Start
```bash
npm install -g @openai/codex # Alternatively: `brew install codex`
codex
```

#### Reasoning high
```sh
codex -m gpt-5 -c model_reasoning_effort="high"
```

#### Ollama

[ollama download](https://ollama.com) - open models
```sh
codex --oss -m gpt-oss:20b
```

### Requirements
- Node.js and npm
- ChatGPT Plus, Pro, or Team account
- macOS or Linux (Windows via WSL)

### Configuration

`~/.codex/config.toml`
```sh
[model_providers.gemini]
name = "gemini"
base_url = "https://generativelanguage.googleapis.com/v1beta/openai"
env_key = "GEMINI_API_KEY"

[profiles.gemini]
model_provider = "gemini"
model = "gemini-2.5-pro"
```

#### after config

```sh
codex --profile gemini
```
</details>

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

## GUI & Web Interface Extensions

### Official Web Interface
- [Codex Web](https://chatgpt.com/codex) - Official cloud-based agent with web interface
- Cloud Codex - Sandbox environments preloaded with repositories (ChatGPT Pro/Enterprise/Team/Plus users)

### GUI Desktop Applications
- [Codexia](https://github.com/milisp/codexia) - Modern GUI for OpenAI Codex CLI with multi-session support and real-time streaming (Tauri v2)

### IDE Integrations
- **VS Code**: Run in integrated terminal, create custom tasks
- **Aider Composer**: VS Code extension for Codex-like functionality

## Use Cases

### Development Tasks
- **Refactoring**: Modernize legacy code and improve structure
- **Testing**: Generate comprehensive test suites
- **Bug Fixes**: Identify and resolve issues quickly
- **Documentation**: Generate and maintain code documentation
- **Feature Development**: Scaffold new features and components

### Specialized Tasks
- **Frontend Development**: React components, CSS generation, responsive designs
- **Data Analysis**: Dataset exploration, Python scripting, ML projects
- **Code Understanding**: Legacy code analysis, code reviews, architecture insights

## Community

### Discussions
- [Hacker News Discussion](https://news.ycombinator.com/item?id=43708025) - Community reactions and experiences
- [Machine Learning Mastery](https://machinelearningmastery.com/understanding-openai-codex-cli-commands/) - Understanding CLI commands

### Learning Resources
- [Apidog Blog](https://apidog.com/blog/openai-codex-cli/) - Open source coding agent overview
- Community tutorials and examples (contribute yours!)

### Community Projects
- [Plux](https://github.com/milisp/plux) - AI finder/explorer with visual file tree and one-click @files to AI context
- [MCP-Linker](https://github.com/milisp/mcp-linker) - Cross-platform GUI for managing MCP configs across AI clients
- [awesome-claude-dxt](https://github.com/milisp/awesome-claude-dxt) - Curated list of Claude Desktop Extensions
- [awesome-gpt-oss](https://github.com/milisp/awesome-gpt-oss) - Curated GPT open-source resources and tools
- [awesome-chatgpt-claude-agents](https://github.com/milisp/awesome-chatgpt-claude-agents) - A curated collection of awesome ChatGPT & Claude agents, subagents, and AI-powered development tools

## Contributing

This is an awesome list! Contributions are welcome. Please:

1. Read the [contribution guidelines](contributing.md) first
2. Check existing resources to avoid duplicates
3. Ensure links are working and relevant
4. Follow the established format
5. Submit a pull request with clear descriptions

## Related Projects

- [GitHub Copilot](https://github.com/features/copilot) - AI pair programmer
- [Cursor](https://cursor.sh/) - AI-powered code editor
- [Continue](https://continue.dev/) - Open-source AI code assistant
- [Codeium](https://codeium.com/) - Free AI code completion

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work.