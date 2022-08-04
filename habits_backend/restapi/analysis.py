"""Analysis endpoints for REST API."""

from fastapi import APIRouter

from habits_backend.database.connectors import *
from habits_backend.services.analysis import analysis_service

# TODO: Schema responses

router = APIRouter(
    prefix="/analysis",
    tags=["analysis"],
    responses={404: {"description": "Not found"}})


# Http GET method
@router.get("/tracked", response_model=list[dict])
async def get_tracked_habits():
    """Get all tracked habits."""
    with get_db() as session:
        tracked = analysis_service.get_tracked_habits()

    return tracked


# Http GET method
@router.get("/equal_periodicity/{frequency}", response_model=list[dict])
async def get_equal_periodicity(frequency):
    """Get all habits with the same periodicity."""
    with get_db() as session:
        tracked = analysis_service.get_equal_periodicity(frequency)

    return tracked


# Http GET method
@router.get("/streak/{habit_id}", response_model=dict)
async def get_streak_by_habit_id(habit_id):
    """Get the longest streak for a habit by id."""
    with get_db() as session:
        streak = analysis_service.get_streak_by_habit_id(habit_id)

    return streak


# Http GET method
@router.get("/streak", response_model=dict)
async def get_longest_streak():
    """Get the habit with the longest streak. Search all habits."""
    with get_db() as session:
        streak = analysis_service.get_longest_streak()

    return streak
