from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timedelta


DAY = timedelta(days=1)


def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def safe_birthday_in_year(birth_month: int, birth_day: int, year: int) -> date:
    """
    Return the birthday date for the given year.
    Feb 29 birthdays map to Feb 29 on leap years, Feb 28 otherwise.
    """
    if birth_month == 2 and birth_day == 29 and not is_leap_year(year):
        return date(year, 2, 28)
    return date(year, birth_month, birth_day)


@dataclass(frozen=True)
class BirthdayInfo:
    weekday_born: str
    days_since_last: int
    days_until_next: int
    last_birthday: date
    next_birthday: date
    age_on_next: int
    days_since_birth: int


def calculate_birthday_info(birth: date, today: date | None = None) -> BirthdayInfo:
    """
    Compute weekday of birth, days since last bday, days until next, and age on next.
    """
    if today is None:
        today = date.today()

    # Normalize input (ensure date instance)
    if not isinstance(birth, date):
        raise TypeError("birth must be a datetime.date")

    # Guard impossible dates like Feb 30 via Python's constructor at call site.

    weekday_born = birth.strftime("%A")

    # Determine last and next birthday relative to today.
    this_year_bday = safe_birthday_in_year(birth.month, birth.day, today.year)

    if this_year_bday < today:
        last_bday = this_year_bday
        next_bday = safe_birthday_in_year(birth.month, birth.day, today.year + 1)
    elif this_year_bday > today:
        next_bday = this_year_bday
        last_bday = safe_birthday_in_year(birth.month, birth.day, today.year - 1)
    else:
        # Today is birthday
        last_bday = today
        next_bday = safe_birthday_in_year(birth.month, birth.day, today.year + 1)

    days_since = (today - last_bday).days
    days_until = (next_bday - today).days

    age_on_next = next_bday.year - birth.year
    days_since_birth = (today - birth).days

    return BirthdayInfo(
        weekday_born=weekday_born,
        days_since_last=days_since,
        days_until_next=days_until,
        last_birthday=last_bday,
        next_birthday=next_bday,
    age_on_next=age_on_next,
    days_since_birth=days_since_birth,
    )
