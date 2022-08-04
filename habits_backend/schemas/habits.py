"""
pydantic schema for habits used for data parsing and validation.
"""
from pydantic import BaseModel

from .frequencies import Frequency


class HabitBase(BaseModel):
    """The Habit base class."""
    name: str
    description: str | None = None


class HabitCreate(HabitBase):
    """HabitCreate subclass derived from the HabitBase class."""
    frequency_id: int


class HabitUpdate(HabitBase):
    """HabitUpdate subclass derived from the HabitBase class."""
    id: int


class Habit(HabitBase):
    """Habit subclass derived from the HabitBase class."""
    id: int
    frequency: Frequency

    class Config:
        orm_mode = True
