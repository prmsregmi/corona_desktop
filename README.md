# corona-desktop

A lightweight Windows desktop overlay that displays live COVID-19 statistics directly on your desktop background. Stats are fetched in real-time from [Worldometers](https://www.worldometers.info/coronavirus/) and shown as a transparent, non-interactive overlay in the top-right corner of your screen.

## Features

- Displays live global COVID-19 case counts: Total Cases, Deaths, and Recoveries
- Shows percentage breakdowns relative to total cases
- Two modes: interactive window (`corona.py`) and background overlay (`corona_bg.pyw`)
- Transparent overlay — clicks pass through, no taskbar clutter
- Auto-refreshes every 10 seconds
- Works best with a dark-themed wallpaper

## Requirements

- Windows (uses Win32 API for the transparent overlay)
- Python 3.13+
- [uv](https://docs.astral.sh/uv/) for dependency management

## Installation

### Using uv (recommended)

```bash
# Install uv if you haven't already
pip install uv

# Clone the repository
git clone https://github.com/prmsregmi/corona_desktop.git
cd corona_desktop

# Install dependencies
uv sync
```

### Running

**Background overlay** (runs silently, no console window):
```bash
uv run pythonw corona_bg.pyw
```

**Interactive window** (with console):
```bash
uv run python corona.py
```

## Configuration

Open `corona.py` or `corona_bg.pyw` and look for the comment markers:

- **Change text color**: Find `fg='white'` in the Label definition and change to any Tkinter color
- **Always on top**: Uncomment the `wm_attributes("-topmost", True)` line
- **Position**: The overlay is placed at the top-right by default; adjust the geometry string to reposition

## How It Works

The app scrapes the global counters from Worldometers using `BeautifulSoup` and renders them as a Tkinter label with a transparent background. Windows-specific APIs (`pywin32`) are used to make the window click-through, non-activatable, and layered — so it sits on your desktop without interfering with normal use.

## License

MIT — see [LICENSE](LICENSE)
