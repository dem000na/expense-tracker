from models import Entry
from save_load_commands import save_data, load_data


def add_item(entry: Entry) -> None:
    entries: list | list[Entry] = load_data()
    entries.append(entry)
    save_data(entries)
    print(f'Added: {entry.amount} {entry.category} {entry.note if entry.note != '' else ''} — {entry.date}')

def show_list(category: str) -> None:
    entries: list | list[Entry] = load_data()

    if not entries:
        print("No added items.")

    if category:
        entries = [entry for entry in entries if entry.category.lower() == category.lower()]

    for e in reversed(entries):
        print(e)