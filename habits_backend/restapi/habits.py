"""Habits endpoints."""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

import habits_backend.schemas.habits as schemas
from habits_backend.database.connectors import *
from habits_backend.services.habits import habits_service

router = APIRouter(
    prefix="/habits",
    tags=["habits"],
    responses={404: {"description": "Not found"}})


# Http GET method
@router.get("", response_model=list[schemas.Habit])
async def get_all(skip: int = 0, limit: int = 100):
    """Get all the habits."""
    with get_db() as session:
        habits = habits_service.get_all(skip=skip, limit=limit)

    return habits


# Http GET method
@router.get("/{id}", response_model=schemas.Habit)
async def get_by_id(habit_id):
    """Get habit by id."""
    with get_db() as session:
        habit = habits_service.get_by_id(habit_id)
    # Return the habit or Http 404 response if it's not found
    return habit if habit is not None else JSONResponse(status_code=404, content={"message": "Habit not found"})


# Http POST method
@router.post("", response_model=schemas.Habit)
async def create_habit(habit: schemas.HabitCreate):
    """Create a habit."""
    return habits_service.create(habit=habit)


# Http PUT method
@router.put("", response_model=schemas.Habit)
async def update_habit(habit: schemas.HabitUpdate):
    """Update the habit."""
    updated = habits_service.update(habit=habit)
    # Update the habit and return Http 200 response for success or Http 404 response if the habit is not found
    return JSONResponse(status_code=200, content={"message": "Updated"}) if updated is not None else JSONResponse(
        status_code=404, content={"message": "Habit not found"})


# Http DELETE method that id as a query string
@router.delete("/{id}")
async def deleted_completed_habit(id: int):
    """Delete the habit and related completed habits."""
    deleted = habits_service.delete(id=id)
    # Delete the habit and return Http 200 response for success or Http 404 response if the habit is not found
    return JSONResponse(status_code=200, content={"message": "Deleted"}) if deleted is not None else JSONResponse(
        status_code=404, content={"message": "Habit not found"})
