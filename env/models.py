# env/models.py

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class Task(BaseModel):
    """Represents an actionable task extracted from an email."""
    id: str
    description: str
    priority: int = Field(..., ge=1, le=5)
    completed: bool = False


class Email(BaseModel):
    id: str
    subject: str
    body: str
    sender: str
    received_at: datetime = datetime.now()
    tasks: List[Task] = []
    label: Optional[str] = None

    # Tasks extracted from email
    tasks: List[Task] = []

    # Optional classification label (for grading)
    label: Optional[str] = None