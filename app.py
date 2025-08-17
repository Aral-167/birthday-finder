from __future__ import annotations

from datetime import date
from typing import Optional

from flask import Flask, jsonify, redirect, render_template, request, url_for
import calendar as pycalendar

# Use the shared core logic
from python_app.birthday_core import calculate_birthday_info

app = Flask(__name__)

@app.template_filter('comma')
def comma_filter(n: int) -> str:
    try:
        return f"{int(n):,}"
    except Exception:
        return str(n)


def parse_ymd(value: str) -> Optional[date]:
    try:
        y, m, d = map(int, value.split("-"))
        return date(y, m, d)
    except Exception:
        return None


@app.get("/")
def index():
    return render_template("index.html", today=date.today(), active_page="home")


@app.route("/calc", methods=["GET", "POST"])
def calc():
    if request.method == "POST":
        b = (request.form.get("birthday", "") or "").strip()
    else:
        b = (request.args.get("birthday", "") or "").strip()

    birth = parse_ymd(b)
    if not birth:
        return render_template("index.html", error="Please enter a valid date (YYYY-MM-DD).", today=date.today()), 400

    today_d = date.today()
    if birth > today_d:
        return render_template("index.html", error="Birthday cannot be in the future.", today=today_d), 400

    info = calculate_birthday_info(birth, today_d)
    return render_template(
        "result.html",
        birth=birth,
        info=info,
        active_page="result",
    )


@app.get("/api/calc")
def api_calc():
    b = request.args.get("birthday", "").strip()
    birth = parse_ymd(b)
    if not birth:
        return jsonify({"error": "Invalid birthday. Use YYYY-MM-DD."}), 400

    today_param = request.args.get("today")
    today = parse_ymd(today_param) if today_param else None

    if today is None:
        today = date.today()
    if birth > today:
        return jsonify({"error": "Birthday cannot be in the future."}), 400

    info = calculate_birthday_info(birth, today)
    return jsonify(
        {
            "weekday_born": info.weekday_born,
            "days_since_last": info.days_since_last,
            "days_until_next": info.days_until_next,
            "last_birthday": info.last_birthday.isoformat(),
            "next_birthday": info.next_birthday.isoformat(),
            "age_on_next": info.age_on_next,
            "days_since_birth": info.days_since_birth,
        }
    )


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/calendar")
def calendar_page():
    today = date.today()
    try:
        year = int(request.args.get("year", today.year))
        month = int(request.args.get("month", today.month))
    except Exception:
        year, month = today.year, today.month

    # Normalize month/year
    while month < 1:
        month += 12
        year -= 1
    while month > 12:
        month -= 12
        year += 1

    cal = pycalendar.Calendar(firstweekday=0)  # Monday=0? In Python, by default Monday=0; but display is fine
    weeks = cal.monthdayscalendar(year, month)  # list of weeks; zeros are days outside month

    # Prev/next month
    prev_year, prev_month = (year - 1, 12) if month == 1 else (year, month - 1)
    next_year, next_month = (year + 1, 1) if month == 12 else (year, month + 1)

    month_name = pycalendar.month_name[month]

    return render_template(
        "calendar.html",
        year=year,
        month=month,
        month_name=month_name,
        weeks=weeks,
        prev_year=prev_year,
        prev_month=prev_month,
        next_year=next_year,
        next_month=next_month,
    today=today,
        active_page="calendar",
    )


if __name__ == "__main__":
    app.run(debug=True)
