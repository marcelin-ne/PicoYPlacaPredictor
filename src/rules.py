from datetime import time

class Rules:
    """Class representing rules for Pico y Placa."""
    def __init__(self):
        self.rules = {
            'Monday': [1, 2],
            'Tuesday': [3, 4],
            'Wednesday': [5, 6],
            'Thursday': [7, 8],
            'Friday': [9, 0],
            'Saturday': None,
            'Sunday': None,
            'Holiday': None
        }
        self.time_intervals = {
            'Morning': {'start': time(7, 00), 'end': time(9, 30)},
            'Afternoon': {'start': time(16, 00), 'end':  time(19, 30)}
        }

        @property
        def time_intervals(self):
            return self._time_intervals
        @property
        def rules(self):
            return self._rules

    def get_rule_for_weekday(self, weekday):
        """
        Get the Pico y Placa rule for a specific weekday.

        Parameters:
        - weekday (str): The weekday for which to retrieve the rule.

        Returns:
        - list or None: The Pico y Placa rule for the specified weekday.
        """
        return self.rules.get(weekday)

    def get_morning_interval(self):
        """
        Get the Morning time interval for Pico y Placa.

        Returns:
        - dict: The Morning time interval with 'start' and 'end' keys.
        """

        return self.time_intervals.get('Morning')

    def get_afternoon_interval(self):
        """
        Get the Afternoon time interval for Pico y Placa.

        Returns:
        - dict: The Afternoon time interval with 'start' and 'end' keys.
        """

        return self.time_intervals.get('Afternoon')