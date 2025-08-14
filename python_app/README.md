# Birthday Finder (Python)

Python version with both a GUI (Tkinter) and a CLI.
# Birthday Finder (Python components)

Python components used by the project: a reusable core module, a Tkinter GUI, and a CLI. The Flask web app lives at the project root (`app.py`).

## Structure
- `birthday_core.py` — pure logic functions and dataclass (weekday, days since/until, total days since birth, etc.)

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
- Core logic is covered by tests in `tests/`.
