import pytest
import datetime
from ExpenseTracker.models import Entry
import ExpenseTracker.cli_commands as cli_commands


@pytest.fixture
def entries():
    return [
        Entry(amount=12.5, category='food', note='lunch at cafe', date=datetime.date(2026, 8, 20)),
        Entry(amount=120.0, category='bills', note='electricity', date=datetime.date(2026, 9, 15)),
        Entry(amount=22.0, category='food', note='dinner with friends', date=datetime.date(2026, 10, 1)),
        Entry(amount=10.0, category='games', note='', date=datetime.date(2026, 10, 2)),
        Entry(amount=12.5, category='food', note='lunch at cafe', date=datetime.date(2026, 8, 20)),
        Entry(amount=120.0, category='bills', note='electricity', date=datetime.date(2026, 9, 15)),
        Entry(amount=22.0, category='food', note='dinner with friends', date=datetime.date(2026, 10, 1)),
        Entry(amount=10.0, category='games', note='', date=datetime.date(2026, 10, 2))
    ]

def test_add_item_append_entries(monkeypatch):
    saved: list = []

    monkeypatch.setattr(cli_commands, 'load_data', lambda: [])
    monkeypatch.setattr(cli_commands, 'save_data', lambda e: saved.append(e))

    entry = Entry(amount=12.5, category='food', note='lunch')
    cli_commands.add_item(entry)

    assert saved == [[entry]]

def test_show_list_filter_by_category(monkeypatch, capsys, entries):

    monkeypatch.setattr(cli_commands, 'load_data', lambda: entries)

    cli_commands.show_list(category='food', date=None)

    output = capsys.readouterr().out
    lines = output.splitlines()

    assert len(lines) == 4
    assert 'bills' not in output
    assert 'games' not in output

def test_show_list_filter_by_date(monkeypatch, capsys, entries):

    monkeypatch.setattr(cli_commands, 'load_data', lambda: entries)

    cli_commands.show_list(category='', date=datetime.date(2026, 9, 15))

    output = capsys.readouterr().out
    lines = output.splitlines()

    assert len(lines) == 2
    assert '2026-10-01' not in output

def test_show_month_report(monkeypatch, capsys, entries):

    monkeypatch.setattr(cli_commands, 'load_data', lambda: entries)

    cli_commands.show_month_report(month=None)


    lines = capsys.readouterr().out.splitlines()

    assert lines == [
        'food: €69.00',      # 12.5 + 22 + 12.5 + 22
        'bills: €240.00',    # 120 + 120
        'games: €20.00',     # 10 + 10
        'Total: €329.00'     # 69 + 240 + 20
    ]