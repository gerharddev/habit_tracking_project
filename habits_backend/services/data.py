"""
Defines Data service used to load and delete sample data to the database.
"""
import json
from datetime import time, date, datetime
from typing import Dict, Type, Any

import habits_backend.crud.completed_habits as completed_crud
import habits_backend.crud.frequencies as frequencies_crud
import habits_backend.crud.habits as habits_crud
import habits_backend.schemas.completed_habits as schemas
from habits_backend.database.connectors import *


def _parser(dct, types: Dict[str, Type]):
    """Parse columns in the dict to specified data types
    e.g. str to datetime."""
    if not types:
        return dct

    converters = {
        time: time.fromisoformat,
        date: date.fromisoformat,
        datetime: datetime.fromisoformat
    }

    for key, item_type in types.items():
        func = converters[item_type]
        dct[key] = func(dct[key])
    return dct


def get_data(filename, key_to_type: Dict[str, Type] = None) -> Dict[str, Any]:
    """Loads the data from a json file and parse the data to the correct format"""
    with open(filename) as f:
        return json.load(f, object_hook=lambda dct: _parser(dct, key_to_type))


# Data service class
class DataService:
    """The Data service class."""

    # Declare a class method. Can be called by using data_service.frequencies() (classname.methodname())
    @classmethod
    def frequencies(cls):
        """Load frequencies if they do not exist."""
        with get_db() as session:
            if not frequencies_crud.has_frequencies(session):
                # Load the test data from the json file
                data = get_data("./database/data/frequencies.json")
                if len(data) > 0:
                    return frequencies_crud.recreate_frequencies(db=session, frequencies=data)

    # Declare a class method. Can be called by using classname.methodname()
    @classmethod
    def sample_data(cls):
        """Load sample data to demonstrate application functionality."""

        with get_db() as db:
            cls.load_habits(db)
            cls.load_completed_habits(db)

    # Declare a class method. Can be called by using classname.methodname()
    @classmethod
    def load_habits(cls, db):
        """Load sample habits for demo purposes"""
        # Habits
        data = get_data("./database/data/habits.json")
        dedupe = []
        for item in data:
            # Remove duplicate values
            if habits_crud.get_habit_by_name(db, item["name"]) is None:
                dedupe.append(item)
        habits_crud.create_habits(db, dedupe)

    # Declare a class method. Can be called by using classname.methodname()
    @classmethod
    def load_completed_habits(cls, db):
        """Load sample completed habits for demo purposes"""
        # Completed Habits
        data = get_data("./database/data/completed_habits.json", key_to_type={'completed_date': datetime})
        dedupe = []
        for item in data:
            # Remove duplicate values
            parsed_item = schemas.CompletedHabitCreate.parse_obj(item)
            if not completed_crud.exist(db, parsed_item):
                dedupe.append(item)

        completed_crud.create_list(db, dedupe)

    # Declare a class method. Can be called by using classname.methodname()
    @classmethod
    def clear_database(cls):
        """Clear all Habits and Completed habits from the database."""
        with get_db() as session:
            completed_crud.delete_all(session)
            return habits_crud.delete_all(session)


# Create an instance of the DataService
data_service = DataService()

