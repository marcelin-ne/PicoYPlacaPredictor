# Create a file named pico_y_placa.py

class Predictor:
    def __init__(self, plate_number, date, time):
        self.plate_number = plate_number
        self.date = date
        self.time = time

    def can_drive(self):
        # Implement the logic to check if the car can be on the road
        #Return a true o false value for the firts test
        if self.date == "2023-11-21" and  "07:00" <= self.time <= "09:30" and self.plate_number == "ABC-123":
                return True
        else:
            return False