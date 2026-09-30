import json
from pathlib import Path
from models import Entry

DATA_FILE: Path = Path(__file__).resolve().parent.parent / 'data' / 'entries.json'

def save_data(entries: list | list[Entry]):
    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            data: list[dict[str, float]] = [entry.to_dict() for entry in entries]
            json.dump(data, file, indent=4, ensure_ascii=False)

    except OSError as e:
        print(f"Failed to save entries: {e}")


def load_data() -> list | list[Entry]:
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            data: list[dict] = json.load(file)

            data: list[Entry] = [Entry.from_dict(entry) for entry in data]
            return data

    except json.JSONDecodeError:
        print(f"Warning: {DATA_FILE} is not valid JSON. Starting empty.")
        return []
    except TypeError as e:
        print(f"Warning: {DATA_FILE} has invalid data ({e}). Starting empty.")
        return []