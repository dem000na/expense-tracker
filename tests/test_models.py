from ExpenseTracker.models import Entry
import datetime

def test_entry_defaults_to_today():
    entry = Entry(12.5, 'food', 'lunch')
    assert entry.date == datetime.date.today()

def test_entry_to_dict():
    entry = Entry(12.5, 'food', 'lunch')
    entry_dict = entry.to_dict()
    assert isinstance(entry_dict, dict)

def test_entry_from_dict_to_object():
    entry = Entry.from_dict({"amount": 12.5, "category": "food", "note": "lunch at cafe", "date": "2026-08-20"})
    assert entry.amount == 12.5
    assert entry.category == "food"
    assert entry.note == "lunch at cafe"
    assert entry.date == datetime.date(2026, 8, 20)