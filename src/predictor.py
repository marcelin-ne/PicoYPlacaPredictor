# Create a file named pico_y_placa.py
from datetime import datetime


class Predictor:
    def __init__(self, plate_number, date, time):
        self.plate_number = plate_number
        self.date = date
        self.time = time

    def can_drive(self):
        #weekday = datetime.strptime(self.date, "%Y-%m-%d").weekday()
        weekday = self.get_weekday()
        last_digit = self.get_last_digit()
        #If the day of the week is Monday, Wednesday or Friday and the last digit of the plate is odd and the time is between 07:00 and 09:30
        if weekday in [0, 2, 4] and last_digit % 2 != 0 and "07:00" <= self.time <= "09:30":
            return True
        else:
            return False

    def get_weekday(self):
        return datetime.strptime(self.date, "%Y-%m-%d").weekday()

    def get_last_digit(self):
        return int(self.plate_number[-1])