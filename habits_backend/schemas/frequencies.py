"""
pydantic schema for frequencies used for data parsing and validation.
"""
from enum import Enum

from pydantic import BaseModel


class TimeCode(str, Enum):
    """Define a time code to specify repetition frequency"""
    day = 'day'
    week = 'week'
    month = 'month'


class FrequencyBase(BaseModel):
    """The frequency base class."""
    name: str
    repeat: TimeCode  # FrequencyBase.repeat = TimeCode.day

    class Config:
        # Contains enum values
        use_enum_values = True


class FrequencyCreate(FrequencyBase):
    """Frequency create subclass derived from the FrequencyBase class."""
    # No code, will be exact copy of the base class
    pass


class Frequency(FrequencyBase):
    """Frequency subclass derived from the FrequencyBase class."""
    id: int

    class Config:
        # Support mapping to ORM objects
        orm_mode = True
