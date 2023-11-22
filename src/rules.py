from datetime import time

class Rules:
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

        return self.rules.get(weekday)

    def get_morning_interval(self):

        return self.time_intervals.get('Morning')

    def get_afternoon_interval(self):

        return self.time_intervals.get('Afternoon')