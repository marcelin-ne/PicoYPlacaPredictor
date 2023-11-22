from datetime import datetime
from predictor import Predictor

def get_plate_number():
    return input("Enter the license plate number (format ABC-123): ").strip().upper()

def get_date():
    return input("Enter the date (format YYYY-MM-DD): ").strip()

def get_time():
    return input("Enter the time (format HH:MM): ").strip()

def main():
    plate_number = get_plate_number()
    date_str = get_date()
    time_str = get_time()

    try:
        # Validate the format of date and time
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        time_obj = datetime.strptime(time_str, "%H:%M").time()

        predictor = Predictor(plate_number, date_str, time_str)

        if predictor.can_drive():
            print("You can drive your vehicle at this time!")
        else:
            print("You cannot drive your vehicle at this time due to restrictions.")
    except ValueError:
        print("Error: Incorrect date or time format. Please try again.")

if __name__ == "__main__":
    main()
