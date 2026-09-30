# ExpenseTracker

A small command-line app for logging your expenses and listing them later. Entries are stored in a local JSON file, so there is no database and nothing to install beyond Python.

## Features

- Add an expense with an amount, a category and an optional note.
- List all expenses, newest first.
- Filter the list by category.
- The date is set automatically to today.
- Multi-word categories and notes work without quotes.

## Requirements

- Python 3.12 or newer (the code uses nested quotes inside f-strings).
- No third-party packages.

## Setup

```bash
git clone <https://github.com/dem000na/expense-tracker.git>
cd ExpenseTracker
```

Optionally create a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux
```

## Usage

Run the commands from inside the inner `ExpenseTracker` folder, where `cli.py` lives:

```bash
cd ExpenseTracker
```

### Add an expense

```bash
python cli.py add -a 20 -c food
python cli.py add -a 45.50 -c eating out -n dinner with friends
```

| Option | Long form | Required | Description |
|--------|-----------|----------|-------------|
| `-a` | `--amount` | yes | Price of the item (number, e.g. `12.99`) |
| `-c` | `--category` | yes | Category name; may be several words |
| `-n` | `--note` | no | Free-text note; may be several words |

### List expenses

```bash
python cli.py list                 # everything, newest first
python cli.py list -c food         # only the "food" category
python cli.py list -c eating out   # multi-word category
```

Example output:

```
2026-09-30 €45.50 eating out dinner with friends
2026-09-30 €20.00 food
```


### Help

```bash
python cli.py -h
python cli.py add -h
python cli.py list -h
```

## Where is the data stored?

Entries are saved to `data/entrie.json` in the project root. The file and folder are created automatically on the first `add`. The file is listed in `.gitignore` so your personal spending is not pushed to GitHub.

Each entry looks like this:

```json
{
    "amount": 20.0,
    "category": "food",
    "note": "",
    "date": "2026-09-30"
}
```

If the file contains invalid JSON, the app prints a warning and starts with an empty list. The next `add` overwrites the bad file.

## Project structure

```
ExpenseTracker/
├── ExpenseTracker/
│   ├── cli.py                # Entry point: argument parsing (add / list)
│   ├── cli_commands.py        # add_item and show_list logic
│   ├── models.py              # Entry dataclass (to/from dict, display format)
│   └── save_load_commands.py  # Read/write data/entrie.json
├── data/
│   └── entrie.json            # Your saved expenses (git-ignored)
├── .gitignore
└── README.md
```

## Notes

- Amounts are displayed with a euro sign (`€`).
