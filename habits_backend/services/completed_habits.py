"""
Defines Completed Habits service.
"""
from typing import List

import habits_backend.crud.completed_habits as crud
import habits_backend.schemas.completed_habits as schemas
from habits_backend.database.connectors import *


# Completed habits service class
class CompletedHabitsService:
    """The Completed Habit service."""

    # Declare a class method. Can be called by using completed_habits_service.get_by_id (classname.methodname())
    @classmethod
    def get_by_id(cls, habit_id, skip: int = 0, limit: int = 100) -> List[schemas.CompletedHabitQuery]:
        """Returns a completed habit by ID."""
        with get_db() as session:
            db_habits = crud.get_by_id(session, habit_id)
        # For each item in the list parse the data to the orm model and return the results
        return [schemas.CompletedHabitQuery.from_orm(h) for h in db_habits] if db_habits is not None else None

    # Declare a class method. Can be called by using classname.methodname()
    @classmethod
    def get_by_id_detailed(cls, habit_id, skip, limit) -> List[schemas.CompletedHabit]:
        """Returns a completed habit by ID."""
        with get_db() as session:
            db_habits = crud.get_by_id_detailed(session, habit_id)
        # For each item in the list parse the data to the orm model and return the results
        habits = [schemas.CompletedHabit.from_orm(h) for h in db_habits]
        return habits

    # Declare a class method. Can be called by using classname.methodname()
    @classmethod
    def get_all(cls, skip, limit) -> List[schemas.CompletedHabitQuery]:
        """Returns a list of completed habits ordered by completed date."""
        with get_db() as session:
            db_habits = crud.get_all(session, skip, limit)
        # For each item in the list parse the data to the orm model and return the results
        habits = [schemas.CompletedHabitQuery.from_orm(h) for h in db_habits]
        return habits

    # Declare a class method. Can be called by using classname.methodname()
    @classmethod
    def create(cls, completed_habit: schemas.CompletedHabitCreate):
        """Create a new completed habit."""
        with get_db() as session:
            results = crud.create(db=session, completed_habit=completed_habit)
            return results

    # Declare a class method. Can be called by using classname.methodname()
    @classmethod
    def delete(cls, id: int):
        """Delete item by id."""
        with get_db() as session:
            return crud.delete(db=session, id=id)


# Create an instance of the CompletedHabitsService
completed_habits_service = CompletedHabitsService()
