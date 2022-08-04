"""This file contains the model declarations used for saving the data."""
from sqlalchemy import Column, Integer, String

from habits_backend.database.connectors import Base


class Frequency(Base):
    __tablename__ = "frequencies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    repeat = Column(String)  # day, week, month or year

