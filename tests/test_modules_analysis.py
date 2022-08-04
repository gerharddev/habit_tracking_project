import datetime
import habits_backend.modules.analysis as analysis

# Test data
habit = {
    "count": 0,
    "repeated": "Daily"
}


def test_is_tracked_true():
    """Test that is_tracked return true if the count is greater than 0."""
    habit["count"] = 1
    value = analysis.is_tracked(habit)
    assert value is True


def test_is_tracked_false():
    """Test that is_tracked return false if the count is 0."""
    habit["count"] = 0
    value = analysis.is_tracked(habit)
    assert value is False


def test_is_equal_period_true():
    """Test if a habit has the same periodicity as the frequency."""
    habit["repeated"] = "Daily"
    frequency = "DAILY"
    value = analysis.is_equal_period(habit, frequency)
    assert value is True


def test_is_equal_period_false():
    """Test if a habit has the different periodicity as the frequency."""
    habit["repeated"] = "weekly"
    frequency = "daily"
    value = analysis.is_equal_period(habit, frequency)
    assert value is False


# Day tests
def test_diff_days_less_than_one_day():
    """Test if the difference between two dates is one day."""
    date1 = datetime.datetime(2022, 4, 29, 14, 17, 45)
    date2 = datetime.datetime(2022, 4, 29, 23, 17, 45)
    value = analysis.diff_days(date1, date2)
    assert value == 0


def test_diff_days_one_day_exact():
    """Test if the difference between two dates is one day."""
    date1 = datetime.datetime(2022, 4, 29, 14, 17, 45)
    date2 = datetime.datetime(2022, 4, 30, 14, 17, 45)
    value = analysis.diff_days(date1, date2)
    assert value == 1


def test_diff_days_one_day_25_hours():
    """
    Test if the difference between two dates is one day.
    Should still return 1. Only the days is taken into consideration for the test.
    """
    date1 = datetime.datetime(2022, 4, 29, 14, 17, 45)
    date2 = datetime.datetime(2022, 4, 30, 15, 17, 45)
    value = analysis.diff_days(date1, date2)
    assert value == 1


def test_diff_days_two_days():
    """
    Test if the difference between two dates is two day.
    Should still return 2. Only the days is taken into consideration for the test.
    """
    date1 = datetime.datetime(2022, 4, 29, 14, 17, 45)
    date2 = datetime.datetime(2022, 5, 1, 15, 17, 45)
    value = analysis.diff_days(date1, date2)
    assert value == 2


def test_diff_days_one_day_year():
    """
    Test if the difference between two dates is 366 days.
    """
    date1 = datetime.datetime(2022, 4, 29, 14, 17, 45)
    date2 = datetime.datetime(2023, 4, 30, 15, 17, 45)
    value = analysis.diff_days(date1, date2)
    assert value == 366


# Week tests
def test_diff_weeks_less_than_one_week():
    """Test if the difference between two dates less than one week is valid."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 5, 7, 14, 17, 45)
    value = analysis.diff_weeks(date1, date2)
    assert value == 0


def test_diff_weeks_one_week_exact():
    """Test if the difference between two dates is one week."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 5, 8, 14, 17, 45)
    value = analysis.diff_weeks(date1, date2)
    assert value == 0


def test_diff_weeks_greater_than_one_week():
    """Test if the difference between two dates is greater than one week."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 5, 9, 15, 17, 45)
    value = analysis.diff_weeks(date1, date2)
    assert value == 2


# Month Tests
def test_diff_months_less_than_one_week():
    """Test if the difference between two dates less than one month is valid."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 5, 31, 14, 17, 45)
    value = analysis.diff_months(date1, date2)
    assert value == 0


def test_diff_months_one_month_exact():
    """Test if the difference between two dates is one month."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 6, 1, 14, 17, 45)
    value = analysis.diff_months(date1, date2)
    assert value == 1


def test_diff_months_one_month_not_exact():
    """Test if the difference between two dates is greater than one month."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 6, 9, 15, 17, 45)
    value = analysis.diff_months(date1, date2)
    assert value == 1


def test_diff_months_greater_than_one_month():
    """Test if the difference between two dates is greater than one month."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 7, 9, 15, 17, 45)
    value = analysis.diff_months(date1, date2)
    assert value == 2


# Streak Tests
def test_is_streak_day_true():
    """Test if is_streak returns True for two consecutive days."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 5, 2, 15, 17, 45)
    value = analysis.is_streak(date1, date2, 'day')
    assert value is True


def test_is_streak_day_false():
    """Test if is_streak returns False for two non-consecutive days."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 5, 3, 15, 17, 45)
    value = analysis.is_streak(date1, date2, 'day')
    assert value is False


def test_is_streak_week_true():
    """Test if is_streak returns True for two consecutive weeks."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 5, 8, 15, 17, 45)
    value = analysis.is_streak(date1, date2, 'week')
    assert value is True


def test_is_streak_week_false():
    """Test if is_streak returns False for two non-consecutive weeks."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 5, 14, 15, 17, 45)
    value = analysis.is_streak(date1, date2, 'week')
    assert value is False


def test_is_streak_month_true():
    """Test if is_streak returns True for two consecutive months."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 6, 2, 15, 17, 45)
    value = analysis.is_streak(date1, date2, 'month')
    assert value is True


def test_is_streak_month_false():
    """Test if is_streak returns False for two non-consecutive months."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 7, 3, 15, 17, 45)
    value = analysis.is_streak(date1, date2, 'month')
    assert value is False


# Function Tests
def test_get_equal_periodicity():
    """Test that we find habits with the same periodicity."""
    habits = [{'id': 1, 'name': 'Running', 'repeated': 'Daily', 'count': 9}, {'id': 2, 'name': 'Meditation', 'repeated': 'Daily', 'count': 8}, {'id': 3, 'name': 'PersonalTime', 'repeated': 'Weekly', 'count': 4}]
    value = analysis.get_equal_periodicity(habits, 'daily')
    assert len(value) == 2


def test_get_streak_by_habit_id():
    """Test that we get a streak by habit_id and frequency."""
    from habits_backend.schemas.completed_habits import CompletedHabitQuery

    completed = [CompletedHabitQuery(id=1, completed_date=datetime.datetime(2022, 4, 27, 14, 17, 45), habit_id=1),
                 CompletedHabitQuery(id=2, completed_date=datetime.datetime(2022, 4, 28, 15, 57, 21), habit_id=1),
                 CompletedHabitQuery(id=3, completed_date=datetime.datetime(2022, 4, 29, 14, 17, 45), habit_id=1),
                 CompletedHabitQuery(id=4, completed_date=datetime.datetime(2022, 4, 30, 15, 57, 21), habit_id=1),
                 CompletedHabitQuery(id=5, completed_date=datetime.datetime(2022, 5, 1, 14, 17, 45), habit_id=1),
                 CompletedHabitQuery(id=6, completed_date=datetime.datetime(2022, 5, 2, 15, 57, 21), habit_id=1),
                 CompletedHabitQuery(id=7, completed_date=datetime.datetime(2022, 5, 4, 15, 57, 21), habit_id=1),
                 CompletedHabitQuery(id=8, completed_date=datetime.datetime(2022, 5, 5, 15, 57, 21), habit_id=1),
                 CompletedHabitQuery(id=9, completed_date=datetime.datetime(2022, 5, 6, 15, 57, 21), habit_id=1)]
    value = analysis.get_streak_by_habit_id(completed, 'day')
    # Should find a streak of 6 days
    assert value['cnt'] == 6
