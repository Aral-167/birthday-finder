from __future__ import annotations

import argparse
from datetime import date

try:
    from .birthday_core import calculate_birthday_info
except ImportError:  # allow running as script
    from birthday_core import calculate_birthday_info


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Birthday Finder CLI")
    p.add_argument("birthday", help="Your birthday in YYYY-MM-DD format, e.g., 1990-08-13")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        y, m, d = map(int, args.birthday.split("-"))
        birth = date(y, m, d)
    except Exception:
        print("Invalid date. Please use YYYY-MM-DD.")
        return 2

    info = calculate_birthday_info(birth)
    print(f"Weekday you were born: {birth:%A}")
    print(f"Days since last birthday: {info.days_since_last}")
    print(f"Last birthday: {info.last_birthday:%A, %B %d, %Y}")
    print(f"Days until next birthday: {info.days_until_next}")
    print(f"Next birthday: {info.next_birthday:%A, %B %d, %Y}")
    print(f"Age on next birthday: {info.age_on_next}")
    print(f"Total days since birth: {info.days_since_birth}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
