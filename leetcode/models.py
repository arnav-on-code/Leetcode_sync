from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Submission:
    id: str
    title: str
    slug: str
    timestamp: int

    @property
    def date(self):
        return datetime.fromtimestamp(self.timestamp)