from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List


# Unsolvable circular import
class Performance(Enum):
    """A standard to represent the performance of students."""

    NOT_STARTED = 0
    ATTEMPTED = 1
    FAMILIAR = 2
    PROFICIENT = 3
    MASTERED = 4


class Assignment(BaseModel):
    """Assignment model for API."""

    id: int
    name: str
    description: str
    teacher_id: int
    question_ids: List[int]
    due_date: Optional[datetime] = None


class Class(BaseModel):
    """Class model for API."""

    id: int
    name: str
    enter_code: str
    teacher_id: int


class ClassData(BaseModel):
    """Class data model for API."""

    class_name: str
    teacher_name: str
    to_do_assignments: List[Assignment]
    done_assignments: List[Assignment]


class FeedBack(BaseModel):
    """Feedback model for API."""

    comment: str
    performance: "Performance"
