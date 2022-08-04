"""
CRUD operations for analysis class.
"""
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

import habits_backend.models.completed_habit as completed_models
import habits_backend.models.frequency as frequency_models
import habits_backend.models.habit as habit_models


def add_tracking_count(db, habit):
    """Add the completed count to the habit object."""
    query = select(func.count(completed_models.CompletedHabit.id)).where(completed_models.CompletedHabit.habit_id ==
                                                                         habit.id)
    count = db.execute(query).scalar()
    # _asdict() returns a dictionary from the habit object
    results = habit._asdict()
    results["count"] = count
    # Return the habit with the count added
    return results


def get_habit_with_details(db: Session):
    """Get all the habits with their metadata."""
    query = select(habit_models.Habit.id, habit_models.Habit.name, frequency_models.Frequency.name.label(
        "repeated")).join(habit_models.Habit.frequency)
    habits = db.execute(query).all()
    results = [(lambda h:  add_tracking_count(db, h))(h) for h in habits]

    return results
