"""
This file is used for setting up a SQLAlchemy connection to SQLite.
Details: https://docs.sqlalchemy.org/en/14/core/connections.html#basic-usage
"""

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

# Set the database connection string
SQLALCHEMY_DATABASE_URL = "sqlite:///./habits_tracking.db"
Base = declarative_base()


def make_engine() -> Engine:
    """Return an Engine object. """
    return create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


def get_db() -> Session:
    """Returns a new Session on App DB."""
    session = sessionmaker(make_engine(), expire_on_commit=False)
    return session()
