# Add the 'src' directory to the Python path
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.date_manager import  HolidayChecker
from src.predictor import Predictor
from src.rules import Rules
from datetime import datetime


@pytest.fixture
def mock_predictor():
    return Predictor("ABC123", "2023-11-22", "08:30")

def test_get_necessary_values(mock_predictor):
    values = mock_predictor._get_necessary_values("2023-11-22", "08:30")

    assert values['weekday'] == 0  # Ajusta según el día de la semana esperado
    assert values['last_digit'] == 3  # Ajusta según el último dígito esperado
    assert values['time'] == datetime.strptime("08:30", "%H:%M").time()
    # Asegúrate de ajustar los valores según lo esperado para los intervalos y reglas.
    assert values['morning_interval'] == {'start': datetime.strptime("07:00", "%H:%M").time(), 'end': datetime.strptime("09:30", "%H:%M").time()}
    assert values['afternoon_interval'] == {'start': datetime.strptime("16:00", "%H:%M").time(), 'end': datetime.strptime("19:30", "%H:%M").time()}
    assert values['weekday_rule'] == {'digit1': 1, 'digit2': 2}  # Ajusta según las reglas esperadas
    assert values['is_holiday'] == False  # Ajusta según si la fecha es un día festivo o no

def test_can_drive(mock_predictor, mocker):
    mocker.patch.object(Rules, 'get_morning_interval', return_value={'start': datetime.strptime("07:00", "%H:%M").time(), 'end': datetime.strptime("09:30", "%H:%M").time()})
    mocker.patch.object(Rules, 'get_afternoon_interval', return_value={'start': datetime.strptime("16:00", "%H:%M").time(), 'end': datetime.strptime("19:30", "%H:%M").time()})
    mocker.patch.object(Rules, 'get_rule_for_weekday', return_value={'digit1': 1, 'digit2': 2})
    mocker.patch.object(HolidayChecker, 'is_holiday', return_value=False)

    result = mock_predictor.can_drive()

    assert result == False


def test_get_last_digit():
    #scenario 1: Get the last digit of the plate
    predictor = Predictor("ABC-123", "2023-11-20", "08:30")
    assert predictor.get_last_digit() == 3