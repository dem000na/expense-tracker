from models import Entry
from save_load_commands import save_data, load_data
from collections import Counter


def add_item(entry: Entry) -> None:
    entries: list | list[Entry] = load_data()
    entries.append(entry)
    save_data(entries)
    print(f'Added: {entry.amount} {entry.category} {entry.note if entry.note != '' else ''} — {entry.date}')

def show_list(category: str, date) -> None:
    entries: list | list[Entry] = load_data()

    if category:
        entries = [entry for entry in entries if entry.category.lower() == category.lower()]

    if date:
        entries = [entry for entry in entries if entry.date == date]

    if not entries:
        print("No added items.")

    for e in reversed(entries):
        print(e)

def show_month_report(month):
    entries = load_data()
    if month:
        entries = [entry for entry in entries if entry.date.year == month.year and entry.date.month == month.month]

        if not entries:
            print("No added items")
            return

    totals = Counter()

    for entry in entries:
        totals[entry.to_dict()['category']] += entry.to_dict()['amount']

    for key, value in totals.items():
        print(f"{key}: €{value:.2f}")

    
    print(f'Total: €{sum(totals.values()):.2f}')


    

    