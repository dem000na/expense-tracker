from dataclasses import dataclass, asdict, field
import datetime

@dataclass
class Entry:
    amount: float
    category: str
    note: str
    date: datetime.date = field(default_factory=datetime.date.today)

    def to_dict(self):
        data = asdict(self)
        data['date'] = self.date.isoformat()
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            amount=data['amount'],
            category=data['category'],
            note=data['note'],
            date=datetime.date.fromisoformat(data['date'])
        )

    def __str__(self):
        return f'{self.date} €{self.amount:.2f} {self.category} {self.note if self.note != '' else ''}'