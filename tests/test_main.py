"""Sample unit tests to automate testing."""
from click.testing import CliRunner

from habits_backend.main import *

runner = CliRunner()


def test_seed_data():
    """Test the seeding of data."""
    result = runner.invoke(data_seed)
    # Will return true if the result code is 0. Indicating it passed
    assert result.exit_code == 0


def test_rest_api():
    """Test the REST API startup."""
    result = runner.invoke(start_rest_api)
    # Will return true if the result code is 0. Indicating it passed
    assert result.exit_code == 0


def test_analyse_streak_habit():
    """Test the analysis of a streak."""
    result = runner.invoke(analyse_streak_habit, ['--habit_id', 1])
    # Will return true if the result code is 0. Indicating it passed
    assert result.exit_code == 0
