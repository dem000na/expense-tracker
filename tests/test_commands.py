import pytest
from ExpenseTracker.models import Entry
import ExpenseTracker.cli_commands as cli_commands


@pytest.fixture
def entries():
    return [{
        "amount": 12.5,
        "category": "food",
        "note": "lunch at cafe",
        "date": "2026-08-20"
    },
    {
        "amount": 45.0,
        "category": "transport",
        "note": "monthly bus pass",
        "date": "2026-08-20"
    },
    {
        "amount": 8.99,
        "category": "entertainment",
        "note": "movie rental",
        "date": "2026-08-20"
    }]

def test_add_item_append_entries(monkeypatch):
    saved = []

    monkeypatch.setattr(cli_commands, 'load_data', lambda: [])
    monkeypatch.setattr(cli_commands, 'save_data', lambda e: saved.append(e))

    entry = Entry(amount=12.5, category='food', note='lunch')
    cli_commands.add_item(entry)

    assert saved == [[entry]]