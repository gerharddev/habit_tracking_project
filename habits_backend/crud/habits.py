"""
CRUD Operations for habits.
"""
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

import habits_backend.models.completed_habit as completed_models
import habits_backend.models.frequency as frequency_model
import habits_backend.models.habit as models
import habits_backend.schemas.habits as schemas


def get_habit_by_id(db: Session, habit_id: int):
    """Get a habit by id."""
    # Select a habit by id and only return one item. Include the frequency details
    query = select(models.Habit).where(models.Habit.id == habit_id).options(joinedload(models.Habit.frequency)).limit(1)
    # Execute the query and return the results
    return db.execute(query).scalar()


def get_habit_by_name(db: Session, name: str):
    """Get a habit by name."""
    query = select(models.Habit).filter(models.Habit.name == name)
    return db.execute(query).scalar()
    # return db.query(models.Habit).filter(models.Habit.name == name).first()


def get_habits(db: Session, skip: int = 0, limit: int = 100):
    """Get a list of habits."""
    query = select(models.Habit).options(joinedload(models.Habit.frequency)).offset(skip).limit(limit)
    return db.execute(query).scalars().all()


def get_habits_ids(db: Session):
    """Get a list of habit ids."""
    query = select(models.Habit.id)
    return db.execute(query).scalars().all()


def get_frequency(db: Session, habit_id: int):
    """Get frequency details (by habit id) for a habit."""
    query = select(frequency_model.Frequency.repeat).where(models.Habit.id == habit_id).join(
        models.Habit.frequency).limit(1)
    return db.execute(query).scalar()


def create_habit(db: Session, habit: schemas.HabitCreate):
    """Create a habit."""
    # Unpacking (mapping fields) from the HabitCreate schema to the Habit model
    db_habit = models.Habit(**habit.dict())
    # Create the habit in the database
    db.add(db_habit)
    # Commit the transaction
    db.commit()
    db.refresh(db_habit)
    return db_habit


def update_habit(db: Session, habit: schemas.HabitUpdate):
    """Update an existing habit."""
    query = (select(models.Habit)
             .where(models.Habit.id == habit.id))
    # Make sure the habit exists
    exist = db.execute(query).scalars().first()
    if exist is None:
        return None

    db.query(models.Habit).filter(models.Habit.id == habit.id).update({'name': habit.name, 'description':
        habit.description})
    db.commit()
    return "Updated"


def create_habits(db: Session, habits: list[dict]):
    """Create multiple habits."""
    # Check that the list of habits contains at least 1 item
    if len(habits) <= 0:
        return
    db.bulk_insert_mappings(models.Habit, habits)
    db.commit()


def delete(db: Session, id: int):
    """Delete the Habit with all the completed habits."""
    # Does the habit exist
    exists = db.query(models.Habit).where(models.Habit.id == id).scalar()
    if exists is None:
        return None  # Nothing found, return None
    # Item found, delete it
    db.query(completed_models.CompletedHabit).where(completed_models.CompletedHabit.habit_id == id).delete()
    db.query(models.Habit).where(models.Habit.id == id).delete()
    db.commit()
    return "Deleted"


def delete_all(db: Session):
    """Delete all the Habits."""
    db.query(models.Habit).delete()
    db.commit()
    return "Deleted"
