# ExpenseTracker

A small command-line app for logging your expenses, listing them and summing them up by category. Entries are stored in a local JSON file, so there is no database and nothing to install beyond Python.

## Features

- Add an expense with an amount, a category and an optional note.
- List all expenses, newest first.
- Filter the list by category and/or by exact date.
- Report totals per category, for everything or for a single month.
- The date is set automatically to today.
- Multi-word categories and notes work without quotes.
- Activity and errors are written to a log file.

## Requirements

- Python 3.12 or newer (the code uses nested quotes inside f-strings).
- No third-party packages to run the app. `pytest` is needed only to run the tests.

## Setup

```bash
git clone https://github.com/dem000na/expense-tracker.git
cd ExpenseTracker
```

Optionally create a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux
```

## Usage

Run the app from the project root (the folder that contains the inner `ExpenseTracker` package) as a module:

```bash
python -m ExpenseTracker.cli <command> [options]  # Example: python -m ExpenseTracker.cli add --amount 20.5 --category food --note lunch
```

### Add an expense

```bash
python -m ExpenseTracker.cli add -a 20 -c food
python -m ExpenseTracker.cli add -a 45.50 -c eating out -n dinner with friends
```

| Option | Long form | Required | Description |
|--------|-----------|----------|-------------|
| `-a` | `--amount` | yes | Price of the item (number, e.g. `12.99`) |
| `-c` | `--category` | yes | Category name; may be several words |
| `-n` | `--note` | no | Free-text note; may be several words |

### List expenses

```bash
python -m ExpenseTracker.cli list                       # everything, newest first
python -m ExpenseTracker.cli list -c food               # only the "food" category
python -m ExpenseTracker.cli list -c eating out         # multi-word category
python -m ExpenseTracker.cli list -d 2026-09-30         # only entries from that day
python -m ExpenseTracker.cli list -c food -d 2026-09-30 # both filters combined
```

| Option | Long form | Description |
|--------|-----------|-------------|
| `-c` | `--category` | Show only this category (case-insensitive; may be several words) |
| `-d` | `--date` | Show only entries from this date, format `YYYY-MM-DD` |

Example output:

```
2026-09-30 €45.50 eating out dinner with friends
2026-09-30 €20.00 food
```

### Report totals per category

```bash
python -m ExpenseTracker.cli report                 # all entries
python -m ExpenseTracker.cli report -m 2026-09      # only September 2026
```

| Option | Long form | Description |
|--------|-----------|-------------|
| `-m` | `--month` | Limit the report to this month, format `YYYY-MM` |

Example output:

```
food: €20.00
eating out: €45.50
Total: €65.50
```

### Help

```bash
python -m ExpenseTracker.cli -h
python -m ExpenseTracker.cli add -h
python -m ExpenseTracker.cli list -h
python -m ExpenseTracker.cli report -h
```

## Where is the data stored?

Entries are saved to `data/entries.json` in the project root. The file and folder are created automatically on the first `add`. Writes are atomic (a temp file is written and then swapped in), so a crash mid-save will not corrupt your data. The file is listed in `.gitignore` so your personal spending is not pushed to GitHub.

Each entry looks like this:

```json
{
    "amount": 20.0,
    "category": "food",
    "note": "",
    "date": "2026-09-30"
}
```

If the file contains invalid JSON or malformed entries, the app logs the error and starts with an empty list. The next `add` overwrites the bad file.

## Logging

Each run writes debug-level logs to `logging/logs.log` in the project root. The file is overwritten on every run and is git-ignored.

## Running the tests

```bash
pip install pytest
python -m pytest
```

Tests live in `tests/` and cover the `Entry` model and the command logic.

## Project structure

```
ExpenseTracker/
├── ExpenseTracker/
│   ├── cli.py                 # Entry point: argument parsing (add / list / report)
│   ├── commands.py            # add_item, show_list and show_month_report logic
│   ├── models.py              # Entry dataclass (to/from dict, display format)
│   └── storage.py             # Read/write data/entries.json
├── tests/
│   ├── test_commands.py
│   └── test_models.py
├── data/
│   └── entries.json           # Your saved expenses (git-ignored)
├── logging/
│   └── logs.log               # Run log (git-ignored)
├── .gitignore
└── README.md
```

## Notes

- Amounts are displayed with a euro sign (`€`).
