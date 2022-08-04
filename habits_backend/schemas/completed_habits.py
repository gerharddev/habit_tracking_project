"""
pydantic schema for completed habits used for data parsing and validation.
"""
from datetime import datetime

from pydantic import BaseModel

from .habits import Habit


class CompletedHabitBase(BaseModel):
    """The CompletedHabitBase class."""
    id: int
    completed_date: datetime


class CompletedHabitQuery(CompletedHabitBase):
    """CompletedHabitQuery subclass derived from the CompletedHabitBase class."""
    habit_id: int

    class Config:
        # Support mapping to ORM objects
        orm_mode = True


class CompletedHabitCreate(BaseModel):
    """CompletedHabitCreate subclass derived from the CompletedHabitBase class."""
    completed_date: datetime
    habit_id: int

    class Config:
        # Support mapping to ORM objects
        orm_mode = True


class CompletedHabit(CompletedHabitBase):
    """CompletedHabit subclass derived from the CompletedHabitBase class."""
    habit: Habit

    class Config:
        # Support mapping to ORM objects
        orm_mode = True
