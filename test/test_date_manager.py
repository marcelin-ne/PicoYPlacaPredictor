import sys
import os
from datetime import date

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.date_manager import DateParser , HolidayChecker


def test_valid_date():
    date_parser = DateParser("2023-11-27")
    weekday = date_parser.get_weekday()
    assert weekday == "Monday"

def test_invalid_date():
    date_parser = DateParser("invalid_date")
    weekday = date_parser.get_weekday()
    assert weekday == "Invalid Date"

def test_valid_holiday():
    holiday_checker = HolidayChecker()
    date_to_check = date(2023, 2, 20)  # CARNAVAL_1
    assert holiday_checker.is_holiday(date_to_check) is True

def test_non_holiday():
    holiday_checker = HolidayChecker()
    date_to_check = date(2023, 1, 3)  # Not a fetive date
    assert holiday_checker.is_holiday(date_to_check) is False