from datetime import date

from python_app.birthday_core import calculate_birthday_info


def test_today_is_birthday():
    birth = date(2000, 8, 13)
    today = date(2025, 8, 13)
    info = calculate_birthday_info(birth, today)
    assert info.days_since_last == 0
    assert info.days_until_next == (date(2026, 8, 13) - today).days
    assert info.age_on_next == 26


def test_before_birthday_in_year():
    birth = date(2000, 12, 25)
    today = date(2025, 8, 13)
    info = calculate_birthday_info(birth, today)
    assert info.days_since_last == (today - date(2024, 12, 25)).days
    assert info.days_until_next == (date(2025, 12, 25) - today).days


def test_after_birthday_in_year():
    birth = date(2000, 2, 10)
    today = date(2025, 8, 13)
    info = calculate_birthday_info(birth, today)
    assert info.days_since_last == (today - date(2025, 2, 10)).days
    assert info.days_until_next == (date(2026, 2, 10) - today).days


def test_feb_29_in_non_leap_year():
    birth = date(2000, 2, 29)
    today = date(2025, 8, 13)  # 2025 not a leap year
    info = calculate_birthday_info(birth, today)
    assert info.last_birthday == date(2025, 2, 28)
    assert info.next_birthday == date(2026, 2, 28)


def test_weekday_format():
    birth = date(1990, 1, 1)  # Monday
    info = calculate_birthday_info(birth, date(2025, 8, 13))
    assert info.weekday_born == "Monday"
