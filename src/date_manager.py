from datetime import datetime , date


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

class HolidayChecker:
    def __init__(self):
        # Diccionario de días festivos
        self.holidays = {
            "NEW_YEAR": date(2023, 1, 2),
            "CARNAVAL_1": date(2023, 2, 20),
            "CARNAVAL_2": date(2023, 2, 21),
            "GOOD_FRIDAY": date(2023, 4, 7),
            "LABOR_DAY": date(2023, 5, 1),
            "PICHINCHA_BATTLE": date(2023, 5, 26),
            "FIRST_CRY_OF_INDEPENDENCE": date(2023, 8, 11),
            "GUAYAQUIL_INDEPENDENCE": date(2023, 10, 9),
            "DAY_OF_THE_DEAD": date(2023, 11, 2),
            "CUENCA_INDEPENDENCE": date(2023, 11, 3),
            "QUITO_FOUNDATION": date(2023, 12, 4),
            "CHRISTMAS": date(2023, 12, 25)
        }

    def is_holiday(self, date_to_check):
        # Verificar si la fecha dada es un día festivo
        return date_to_check in self.holidays.values()

