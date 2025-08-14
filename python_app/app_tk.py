from __future__ import annotations

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

try:
    from .birthday_core import calculate_birthday_info
except ImportError:  # direct run fallback
    from birthday_core import calculate_birthday_info


class BirthdayApp(ttk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master, padding=12)
        self.master.title("Birthday Finder (Python)")
        master.geometry("520x340")
        master.resizable(False, False)

        # Input row
        self.input_var = tk.StringVar()
        row1 = ttk.Frame(self)
        row1.pack(fill="x", pady=(0, 8))
        ttk.Label(row1, text="Your birthday (YYYY-MM-DD)").pack(anchor="w")

        entry_row = ttk.Frame(row1)
        entry_row.pack(fill="x", pady=(4, 0))
        self.entry = ttk.Entry(entry_row, textvariable=self.input_var)
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.insert(0, "2000-01-01")
        ttk.Button(entry_row, text="Check", command=self.on_check).pack(side="left", padx=(8, 0))
        ttk.Button(entry_row, text="Reset", command=self.on_reset).pack(side="left", padx=(8, 0))

        # Results
        self.tree = ttk.Treeview(self, columns=("value",), show="tree")
        self.tree.pack(fill="both", expand=True)
        self.items = {
            "weekday": self.tree.insert("", "end", text="Weekday you were born: —"),
            "days_since": self.tree.insert("", "end", text="Days since last birthday: —"),
            "last": self.tree.insert("", "end", text="Last birthday: —"),
            "days_until": self.tree.insert("", "end", text="Days until next birthday: —"),
            "next": self.tree.insert("", "end", text="Next birthday: —"),
            "age_next": self.tree.insert("", "end", text="Age on next birthday: —"),
            "days_since_birth": self.tree.insert("", "end", text="Total days since birth: —"),
        }

        self.pack(fill="both", expand=True)
        self.entry.focus_set()

    def on_reset(self):
        self.input_var.set("")
        for key, item in self.items.items():
            base = {
                "weekday": "Weekday you were born: —",
                "days_since": "Days since last birthday: —",
                "last": "Last birthday: —",
                "days_until": "Days until next birthday: —",
                "next": "Next birthday: —",
                "age_next": "Age on next birthday: —",
                "days_since_birth": "Total days since birth: —",
            }[key]
            self.tree.item(item, text=base)
        self.entry.focus_set()

    def on_check(self):
        raw = self.input_var.get().strip()
        try:
            y, m, d = map(int, raw.split("-"))
            birth = date(y, m, d)
        except Exception:
            messagebox.showerror("Invalid date", "Please enter a valid date in YYYY-MM-DD format.")
            return

        info = calculate_birthday_info(birth)
        self.tree.item(self.items["weekday"], text=f"Weekday you were born: {birth.strftime('%A')}")
        self.tree.item(self.items["days_since"], text=f"Days since last birthday: {info.days_since_last}")
        self.tree.item(self.items["last"], text=f"Last birthday: {info.last_birthday:%A, %B %d, %Y}")
        self.tree.item(self.items["days_until"], text=f"Days until next birthday: {info.days_until_next}")
        self.tree.item(self.items["next"], text=f"Next birthday: {info.next_birthday:%A, %B %d, %Y}")
        self.tree.item(self.items["age_next"], text=f"Age on next birthday: {info.age_on_next}")
    self.tree.item(self.items["days_since_birth"], text=f"Total days since birth: {info.days_since_birth}")


def main():
    root = tk.Tk()
    # Use platform-native theme if available
    try:
        style = ttk.Style(root)
        if "vista" in style.theme_names():
            style.theme_use("vista")
        elif "clam" in style.theme_names():
            style.theme_use("clam")
    except Exception:
        pass

    BirthdayApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
