# Pico y Placa Predictor

This is a simple Pico y Placa predictor project that helps users determine whether they can drive their vehicles based on license plate number, date, and time.

## Features

- **Pico y Placa Rules:** The system follows specific rules for each day of the week and time intervals to determine if a vehicle can be driven. See the rules in the [Rules section](#rules).

- **User Interaction:** The `main.py` script allows users to input their license plate number, date, and time to check if they can drive.

- **Holiday Handling:** The system considers holidays when determining driving restrictions.

- **Tested with pytest:** Unit tests have been implemented using pytest to ensure the functionality of each component.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/marcelin-ne/PicoYPlacaPredictor.git
   
## Rules 
By day :
- Monday: Last digits 1 and 2
- Tuesday: Last digits 3 and 4
- Wednesday: Last digits 5 and 6
- Thursday: Last digits 7 and 8
- Friday: Last digits 9 and 0
- Saturday: No restrictions
- Sunday: No restrictions
- Holiday: No restrictions.
By time :
- (Hours: 7:00 am - 9:30 am / 4:00 pm - 7:30 pm)

##Requirements
Python 3.x
Visual Studio Code (VSCode) was used for code development.

