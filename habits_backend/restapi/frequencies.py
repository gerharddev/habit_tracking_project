"""Frequencies endpoints."""

from fastapi import APIRouter

import habits_backend.schemas.frequencies as schemas
from habits_backend.services.frequencies import frequencies_service

router = APIRouter(
    prefix="/frequencies",
    tags=["frequencies"],
    responses={404: {"description": "Not found"}})


# Http GET method
@router.get("", response_model=list[schemas.Frequency])
async def get_all_frequencies():
    """Get all frequencies."""
    return frequencies_service.get_all()


