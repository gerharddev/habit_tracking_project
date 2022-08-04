"""
pydantic schema for completed habits metadata used for data parsing and validation.
This is used by the analysis module.
"""

from pydantic import BaseModel


class HabitMetadataBase(BaseModel):
    """Base class for habit metadata."""
    id: int
    name: str


class HabitMetadata(HabitMetadataBase):
    """Habit metadata subclass derived from the HabitMetadataBase class."""
    repeated: str
    count: int

    class Config:
        # Support mapping to ORM objects
        orm_mode = True
