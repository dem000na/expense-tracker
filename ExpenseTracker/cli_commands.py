from models import Entry
from save_load_commands import save_data, load_data


def add_item(entry) -> None:
    entries: list | list[Entry] = load_data()
    entries.append(entry)
    save_data(entries)

def show_list(category):
    entries: list | list[Entry] = load_data()

    if not entries:
        print("No added items.")

    if category:
        entries = [entry for entry in entries if entry.category.lower() == category.lower()]

    for e in sorted(entries, key=lambda entry: entry.date, reverse=True):
        print(e)