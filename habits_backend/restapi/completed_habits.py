"""Completed Habits endpoints."""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

import habits_backend.schemas.completed_habits as schemas
from habits_backend.services.completed_habits import completed_habits_service

router = APIRouter(
    prefix="/completed-habits",
    tags=["completed-habits"],
    responses={404: {"description": "Not found"}})


# Http GET method that will return a CompletedHabitQuery schema object
@router.get("", response_model=list[schemas.CompletedHabitQuery])
async def get_all(skip: int = 0, limit: int = 100):
    """Get a list of all completed habits."""
    completed_habits = completed_habits_service.get_all(skip=skip, limit=limit)

    return completed_habits


# Http GET method that will return a CompletedHabitQuery schema object
@router.get("/{habit-id}", response_model=list[schemas.CompletedHabitQuery])
async def get_by_habit_id(habit_id, skip: int = 0, limit: int = 100):
    completed_habits = completed_habits_service.get_by_id(habit_id, skip=skip, limit=limit)

    return (completed_habits if completed_habits is not None else JSONResponse(status_code=404,
            content={"message": "Nothing found for this habit id"}))


# Http GET method that will return a CompletedHabit schema object
@router.get("/{habit-id}/detailed", response_model=list[schemas.CompletedHabit])
async def get_by_habit_id_detailed(habit_id, skip: int = 0, limit: int = 100):
    completed_habit = completed_habits_service.get_by_id_detailed(habit_id, skip=skip, limit=limit)

    return completed_habit


# Http POST method that expect a CompletedHabitCreate object and will return a CompletedHabit schema object
@router.post("", response_model=schemas.CompletedHabit)
async def create_completed_habit(completed_habit: schemas.CompletedHabitCreate):
    results = completed_habits_service.create(completed_habit=completed_habit)

    # Will return Http response 400 for duplicate or 200 if the insert is successful
    return (JSONResponse(status_code=400, content={"message": "Duplicate - Not inserted"}) if results is "Duplicate"
            else JSONResponse(status_code=200, content={"message": "Completed habit inserted"}))


# Http DELETE method to delete compled habits by id
@router.delete("/{id}")
async def deleted_completed_habit(id: int):
    deleted = completed_habits_service.delete(id=id)

    # Will return Http response 404 if not found or 200 if the deletion was successful
    return JSONResponse(status_code=200, content={"message": "Deleted"}) if deleted is not None else JSONResponse(
        status_code=404, content={"message": "Completed habit not found"})

