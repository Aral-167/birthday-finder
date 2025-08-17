# Birthday Finder

Enter your birthday and get:

- Weekday you were born
- Days since last and until next birthday
- Age on next birthday
- Total days since birth
- Year progress and a timeline between last/next birthdays

UI extras: theme toggle (saved), quick-pick chips (Today/Random/Last used), live preview on the home form (weekday + “Turning N”), inline date validation, copy date/link, native share (when available), toast feedback, and a little confetti on your day. Feb 29 birthdays are handled (Feb 28 in non‑leap years).

## Run the Flask app (Windows PowerShell)

From the project root:

```powershell
# (optional) create & activate a venv
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1

# install deps and run
python -m pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000

- Calendar: http://127.0.0.1:5000/calendar
- Health check: http://127.0.0.1:5000/healthz

Stop with Ctrl+C.

### JSON API

GET `/api/calc?birthday=YYYY-MM-DD`

Returns JSON with weekday, days since/til, last/next birthdays, age on next, and total days since birth.

## Static page (no server)

Open `index.html` directly in your browser:

```powershell
Start-Process "c:\_aral\swPrjs2\birthday_finder\birthday-finder\index.html"
```

## Optional: Desktop and CLI

- Tkinter desktop app:

```powershell
python python_app/app_tk.py
```

- CLI:

```powershell
python python_app/cli.py 1990-08-13
```

## Tests (core logic)

```powershell
python -m pip install -r requirements.txt
python -m pip install pytest
python -m pytest -q
```

## Notes

- Uses local time/timezone for calculations.
- Feb 29 birthdays map to Feb 28 in non‑leap years.
- Clipboard and native share may be limited on some browsers without HTTPS; fallback is copy-to-clipboard.
