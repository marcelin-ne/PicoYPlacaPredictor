import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import time
from src.rules import Rules

def test_get_rule_for_weekday():
    # Definir algunas reglas para la prueba
    test_rules = {
        'Monday': [1, 2],
        'Tuesday': [3, 4],
        'Wednesday': [5, 6],
        'Thursday': [7, 8],
        'Friday': [9, 0],
        'Saturday': None,
        'Sunday': None,
        'Morning': {'start': time(7, 0), 'end': time(9, 30)},
        'Afternoon': {'start': time(16, 0), 'end': time(19, 30)},
        'Holiday': None
    }

    # Crear una instancia de Rules y establecer las reglas
    rules_instance = Rules()
    rules_instance.rules = test_rules

    # Probar obtener reglas para diferentes días de la semana
    assert rules_instance.get_rule_for_weekday('Monday') == [1, 2]
    assert rules_instance.get_rule_for_weekday('Friday') == [9, 0]
    assert rules_instance.get_rule_for_weekday('Saturday') is None  # Regla es None
    assert rules_instance.get_rule_for_weekday('Morning') == {'start': time(7, 0), 'end': time(9, 30)}
    assert rules_instance.get_rule_for_weekday('Afternoon') == {'start': time(16, 0), 'end': time(19, 30)}