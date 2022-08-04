"""Frequencies endpoints."""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from habits_backend.services.data import data_service

router = APIRouter(
    prefix="/data",
    tags=["data"],
    responses={404: {"description": "Not found"}})


# Http POST method
@router.post("/seed")
async def data_seed():
    """Seed testing data."""
    data_service.sample_data()
    return JSONResponse(status_code=200, content={"message": "Loaded the data"})


# Http DELETE method
@router.delete("/clear")
async def data_delete():
    """Delete all testing data."""
    data_service.clear_database()
    return JSONResponse(status_code=200, content={"message": "Deleted"})
