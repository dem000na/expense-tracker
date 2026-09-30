from dataclasses import dataclass, asdict, field
import datetime
from typing import Self

@dataclass
class Entry:
    amount: float
    category: str
    note: str
    date: datetime.date = field(default_factory=datetime.date.today)

    def to_dict(self) -> dict[float, str]:
        data: dict[float, str] = asdict(self)
        data['date'] = self.date.isoformat()
        return data

    @classmethod
    def from_dict(cls, data: list | list[dict[str, float]]) -> Self:
        return cls(
            amount=data['amount'],
            category=data['category'],
            note=data['note'],
            date=datetime.date.fromisoformat(data['date'])
        )

    def __str__(self) -> str:
        return f'{self.date} €{self.amount:.2f} {self.category} {self.note if self.note != '' else ''}'