import json
import os
import tempfile
from pathlib import Path
from models import Entry
from typing import Any

DATA_FILE: Path = Path(__file__).resolve().parent.parent / 'data' / 'entries.json'

def save_data(entries: list | list[Entry]):
    tmp_path: Path | None = None

    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        data: list[dict[str, float]] = [entry.to_dict() for entry in entries]

        fd, tmp_name = tempfile.mkstemp(dir=DATA_FILE.parent, suffix='.tmp')
        tmp_path = Path(tmp_name)

        with os.fdopen(fd, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        os.replace(tmp_path, DATA_FILE)

    except (OSError, TypeError, ValueError) as e:
        if tmp_path is not None:
            tmp_path.unlink(missing_ok=True)
            
        print(f"Failed to save entries: {e}")


def load_data() -> list | list[Entry]:
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            raw_data: list[dict[str, Any]] = json.load(file)
            entries: list[Entry] = [Entry.from_dict(entry) for entry in raw_data]
            return entries

    except json.JSONDecodeError:
        print(f"Warning: {DATA_FILE} is not valid JSON. Starting empty.")
        return []
    except TypeError as e:
        print(f"Warning: {DATA_FILE} has invalid data ({e}). Starting empty.")
        return []