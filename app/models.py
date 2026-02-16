from datetime import date
from typing import Optional

from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False
    due_date: Optional[date] = None
