# Birthday Finder

Enter your birth date and it shows:

- Weekday you were born
- Days since last birthday
- Days until next birthday
- Age on next birthday
- Total days since birth

Feb 29 birthdays are handled: in non-leap years, Feb 28 is used.

## Option A: Python web app (Flask)

From the project root:

```powershell
C:/_aral/swPrjs2/birthday_finder/birthday-finder/.venv/Scripts/python.exe -m pip install -r requirements.txt
C:/_aral/swPrjs2/birthday_finder/birthday-finder/.venv/Scripts/python.exe app.py
```

Open http://127.0.0.1:5000

- Calendar picker: http://127.0.0.1:5000/calendar

Stop with Ctrl+C.

## Option B: Static page (no server)

Open `index.html` directly in your browser:

```powershell
Start-Process "c:\_aral\swPrjs2\birthday_finder\birthday-finder\index.html"
```

## Optional: Desktop and CLI

- Tkinter desktop app:

```powershell
C:/_aral/swPrjs2/birthday_finder/birthday-finder/.venv/Scripts/python.exe python_app/app_tk.py
```

- CLI:

```powershell
C:/_aral/swPrjs2/birthday_finder/birthday-finder/.venv/Scripts/python.exe python_app/cli.py 1990-08-13
```

## Notes

- Uses local time/timezone for calculations.
- Feb 29 birthdays use Feb 28 on non-leap years.
