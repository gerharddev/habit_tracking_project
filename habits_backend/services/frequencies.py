"""
Defines Habits service.

Information:
    pydantic - pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.
    https://pydantic-docs.helpmanual.io/
"""
from typing import List

from fastapi import HTTPException

import habits_backend.crud.frequencies as crud
import habits_backend.schemas.frequencies as schemas
from habits_backend.database.connectors import *


# Frequencies service class
class FrequenciesService:
    """The Frequency service class."""

    # Declare a class method. Can be called by using frequencies_service.get_all() (classname.methodname())
    @classmethod
    def get_all(cls) -> List[schemas.Frequency]:
        """Returns a list of frequencies order by ID."""
        with get_db() as session:
            db_frequencies = crud.get_frequencies(session)
        # For each item in the list parse the data to the orm model and return the results
        frequencies = [schemas.Frequency.from_orm(h) for h in db_frequencies]

        return frequencies

    # Declare a class method. Can be called by using (classname.methodname())
    @classmethod
    def create(cls, frequency: schemas.FrequencyCreate):
        """Create a new frequency."""
        with get_db() as session:
            db_frequency = crud.get_frequency_by_name(session, name=frequency.name)
            if db_frequency:
                # Http response 400 - Duplicate value
                raise HTTPException(status_code=400, detail="Frequency already exist")
        # Return the created frequency
        return crud.create_frequency(db=session, frequency=frequency)


# Create an instance of the FrequenciesService
frequencies_service = FrequenciesService()
