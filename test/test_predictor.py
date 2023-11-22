# Add the 'src' directory to the Python path
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predictor import Predictor


from src.predictor import Predictor

def test_can_drive():
    # Prueba para verificar que la lógica funciona correctamente

    # Escenario 1: Un automóvil con placa que cumple con las restricciones
    predictor = Predictor("ABC-123", "2023-11-21", "08:30")
    assert predictor.can_drive() is True

    # Escenario 2: Un automóvil con placa que no cumple con las restricciones
    predictor = Predictor("XYZ-987", "2023-11-21", "18:00")
    assert predictor.can_drive() is False

    # Agrega más escenarios de prueba según sea necesario
