import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.date_manager import DateParser

def test_valid_date():
    date_parser = DateParser("2023-11-27")
    weekday = date_parser.get_weekday()
    assert weekday == "Monday"

def test_invalid_date():
    date_parser = DateParser("invalid_date")
    weekday = date_parser.get_weekday()
    assert weekday == "Invalid Date"