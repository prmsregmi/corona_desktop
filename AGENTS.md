# corona-desktop — Agent Instructions

## Project Overview

A Windows desktop overlay that scrapes live COVID-19 statistics from Worldometers and renders them as a transparent, click-through, non-interactive Tkinter label on the desktop. Uses `pywin32` for Win32 window styling.

## Tech Stack

- **Language**: Python 3.13+
- **Dependency management**: `uv` — always use `uv add <package>` to add deps, never edit `pyproject.toml` manually or use `pip`
- **Key libraries**: `beautifulsoup4`, `pywin32`, `lxml`
- **Platform**: Windows only (Win32 API for transparent overlay)

## Key Files

- `corona.py` — interactive window version, refreshes every 10 seconds
- `corona_bg.pyw` — background overlay version, no console window, refreshes every 1 second
- `pyproject.toml` — single source of truth for deps and project metadata

## Development

```bash
uv sync                        # install dependencies
uv run python corona.py        # run interactive version
uv run pythonw corona_bg.pyw   # run background overlay (no console)
```

## Git

- Conventional Commits: `feat:`, `fix:`, `chore:`, `refactor:`, etc.
- **Never add a co-author line to commit messages.**
- Commit to a relevant branch (`feat/...`, `fix/...`) off `master`, then push and open a PR.
- Never use `--no-verify` to skip pre-commit hooks.

## Coding Rules

**Simplicity over abstraction** — This is a small display utility. Do not introduce frameworks, CLIs, config systems, or unnecessary patterns.

**No hardcoded secrets** — Any credentials or tokens must come from environment variables.

**Fail clearly** — If a required resource (network, config) is missing, surface a clear message to the user rather than silently degrading.

**Windows-specific code is intentional** — Do not attempt to cross-platform the Win32 API calls unless explicitly asked.

## What NOT to Do

- Do not commit `*.exe`, `.DS_Store`, `.venv/`, or other gitignored files
- Do not remove the `.pyw` extension from `corona_bg.pyw` — it suppresses the console window on Windows
- Do not replace `uv` with `pip` or add a `requirements.txt`
- Do not restructure into a complex src-layout package without a clear reason
- Do not add logging frameworks, argparse, or config file systems unless asked
