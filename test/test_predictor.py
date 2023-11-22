# Add the 'src' directory to the Python path
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predictor import Predictor


def test_can_drive():
    # Scenario 1: A car with a license plate that meets the restrictions
    # Odd last digit, allowed day (Monday)
    predictor_valid = Predictor("ABC-123", "2023-11-20", "08:30")
    assert predictor_valid.can_drive() is True

    # Scenario 2: A car with a license plate that does not meet the restrictions
    # Even last digit, not allowed day (Tuesday)
    predictor_invalid = Predictor("XYZ-987", "2023-11-21", "08:30")
    assert predictor_invalid.can_drive() is False

def test_get_weekday():
    # Scenario 1: Get the weekday for a specific date (Monday)
    predictor = Predictor("ABC-123", "2023-11-20", "08:30")
    assert predictor.get_weekday() == 0  # 0 representa el lunes en la convención de Python

def test_get_last_digit():
    #scenario 1: Get the last digit of the plate
    predictor = Predictor("ABC-123", "2023-11-20", "08:30")
    assert predictor.get_last_digit() == 3