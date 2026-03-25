# CLAUDE.md

This file describes rules and conventions for AI assistants (Claude Code, etc.) working in this repository.

## Project Overview

`corona-desktop` is a Windows desktop overlay that displays live COVID-19 statistics scraped from Worldometers. It uses Tkinter for rendering and `pywin32` for transparent, click-through window behavior.

## Tech Stack

- **Language**: Python 3.13+
- **Dependency management**: [uv](https://docs.astral.sh/uv/) — always use `uv` to add/remove/sync dependencies, never `pip` directly
- **Key libraries**: `beautifulsoup4`, `pywin32`, `lxml`
- **Platform**: Windows only (Win32 API)

## Development Setup

```bash
uv sync           # install dependencies
uv run python corona.py       # run interactive version
uv run pythonw corona_bg.pyw  # run background overlay
```

## Rules for AI Assistants

### General

- Always use `uv add <package>` to add dependencies (never edit `pyproject.toml` deps manually without syncing)
- Never commit a `requirements.txt` — dependency management is done exclusively via `pyproject.toml` + `uv`
- Do not add unnecessary abstractions; this is a small, focused tool — keep it simple
- Preserve the Windows-specific overlay behavior; do not attempt to make it cross-platform unless explicitly asked

### Code Style

- Follow PEP 8 for formatting
- Keep logic minimal — this is a display utility, not a framework
- Comment non-obvious Win32 API calls
- Do not add logging, argparse, or configuration systems unless asked

### Git

- Write clear, imperative commit messages (e.g. `Add auto-refresh interval config`)
- Never commit `.exe`, `.DS_Store`, `.venv`, or other gitignored files
- Keep commits focused — one logical change per commit

### PRs and Reviews

- Tag `@claude` in PR comments or review threads to trigger AI assistance via GitHub Actions
- Describe what changed and why in PR descriptions

### What NOT to Do

- Do not restructure into complex package layouts without a clear reason
- Do not add CLI frameworks, config files, or database layers
- Do not cross-platform-ify the Win32-specific code unless explicitly requested
- Do not remove the `.pyw` extension from `corona_bg.pyw` — it suppresses the console window on Windows
