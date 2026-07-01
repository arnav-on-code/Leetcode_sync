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


@dataclass(slots=True)
class SubmissionDetail:
    submission_id: str

    question_id: str
    title_slug: str

    language: str
    language_verbose: str

    runtime: int
    runtime_display: str

    memory: int
    memory_display: str

    status_code: int

    code: str

    timestamp: int

    @property
    def date(self):
        return datetime.fromtimestamp(self.timestamp)
