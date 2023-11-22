# Create a file named pico_y_placa.py
from datetime import datetime
from date_manager import DateParser, HolidayChecker
from rules import Rules

class Predictor:
    """Class for predicting if a car can drive based on Pico y Placa rules."""

    def __init__(self, plate_number, date, time):
        """
        Initialize the Predictor object.

        Parameters:
        - plate_number (str): The license plate number of the car.
        - date (str): The date in the format 'YYYY-MM-DD'.
        - time (str): The time in the format 'HH:MM'.
        """
        self.plate_number = plate_number
        self.date = date
        self.time = time


    def _get_necessary_values(self, date, time):
        """
        Get necessary values for the prediction.

        Parameters:
        - date (str): The date in the format 'YYYY-MM-DD'.
        - time (str): The time in the format 'HH:MM'.

        Returns:
        - dict: Dictionary containing necessary values for the prediction.
        """
        date_parser = DateParser(date)
        holiday_checker = HolidayChecker()

        weekday = date_parser.get_weekday()
        last_digit = self.get_last_digit()
        time_obj = datetime.strptime(time, "%H:%M").time()
        rules = Rules()
        morning_interval = rules.get_morning_interval()
        afternoon_interval = rules.get_afternoon_interval()
        weekday_rule = rules.get_rule_for_weekday(weekday)
        is_holiday = holiday_checker.is_holiday(date)

        return {
            'weekday': weekday,
            'last_digit': last_digit,
            'time': time_obj,
            'morning_interval': morning_interval,
            'afternoon_interval': afternoon_interval,
            'weekday_rule': weekday_rule,
            'is_holiday': is_holiday
        }

    def can_drive(self):
        """
        Check if the car can drive based on Pico y Placa rules.

        Returns:
        - bool: True if the car can drive, False otherwise.
        """
        # Get necessary values
        values = self._get_necessary_values(self.date, self.time)

        # Logic for verification
        if values['is_holiday'] or values['weekday_rule'] is None or values['last_digit'] not in values['weekday_rule']:
            return True

        # Check if the time is within the restricted time intervals
        is_morning = values['morning_interval']['start'] <= values['time'] <= values['morning_interval']['end']
        is_afternoon = values['afternoon_interval']['start'] <= values['time'] <= values['afternoon_interval']['end']

        # The car can drive if it is not in any of the restricted time intervals
        return not (is_morning or is_afternoon)


    def get_last_digit(self):
        return int(self.plate_number[-1])

