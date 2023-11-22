from datetime import datetime

class DateParser:
    def __init__(self, date):
        self.date = date

    def get_weekday(self):
        try:
            # Try to convert the date string to a datetime object
            date_obj = datetime.strptime(self.date, "%Y-%m-%d")
            # Get the day of the week as a string ("Monday", "Tuesday", etc.)
            return date_obj.strftime("%A")
        except ValueError:
            # Handle the case where the date string is not valid
            return "Invalid Date"

# Example of usage
date_parser = DateParser("2023-11-22")
weekday = date_parser.get_weekday()
print(f"The weekday for the date is: {weekday}")

