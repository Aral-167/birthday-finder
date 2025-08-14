# Birthday Finder (Python)

Python version with both a GUI (Tkinter) and a CLI.

## Structure
- `birthday_core.py` — pure logic functions and dataclass
- `app_tk.py` — Tkinter desktop UI
- `cli.py` — command-line entry
- `tests/` — unit tests for the core logic

## Run (GUI)
```powershell
# from python_app folder
python app_tk.py
```

## Run (CLI)
```powershell
python cli.py 1990-08-13
```

## Tests
```powershell
# requires pytest
python -m pip install pytest
pytest -q
```

Notes:
- Works with Python 3.8+.
- Feb 29 birthdays use Feb 28 on non-leap years.
