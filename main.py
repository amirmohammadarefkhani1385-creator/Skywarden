

"""Observer Log: a simple console program to record astronomy observations."""

import csv
import math
import sqlite3

from observation import Observation, Wavelength_Observation, Brightness_Observation
from visualization import show_exposure_chart
from database import save_observations_to_db

#------------------------------------------------------

observations = []

#------------------------------------------------------

def get_number(prompt, positive=True):
    """Ask for a finite number; return None if the input is invalid."""
    try:
        number = float(input(prompt))
    except ValueError:
        print("Value should be an integer or float number")
        return None

    if not math.isfinite(number) or (positive and number <= 0):
        print("Value must be a finite number" + (" and positive" if positive else ""))
        return None
    return number

#------------------------------------------------------

def add_wavelength_observation():
    """Read the data for a wavelength observation and add it to the list."""
    target = input("Target: ")
    observer = input("Name of observer: ")
    filter_name = input("Filter name: ")
    exposure = get_number("Exposure time (second): ")
    if exposure is None:
        return
    lambda_nm = get_number("Lambda (nm): ")
    if lambda_nm is None:
        return
    observations.append(
        Wavelength_Observation(target, observer, filter_name, exposure, lambda_nm)
    )
    print("Wavelength observation added successfully")
#---------------------------------------------------------

def add_brightness_observation():
    """Read the data for a brightness observation and add it to the list."""
    target = input("Target: ")
    observer = input("Name of observer: ")
    filter_name = input("Filter name: ")
    exposure = get_number("Exposure time (second): ")
    if exposure is None:
        return
    apparent_mag = get_number("Apparent magnitude: ", positive=False)
    if apparent_mag is None:
        return
    observations.append(
        Brightness_Observation(target, observer, filter_name, exposure, apparent_mag)
    )
    print("Brightness observation added successfully")
#------------------------------------------------------------------

def show_observation():
    """Print every stored observation."""
    if not observations:
        print("No observation found")
        return

    for number, obs in enumerate(observations, start=1):
        print(f"\nObservation >>> {number}")
        print(obs.summary())
#------------------------------------------------------------------

def statistical_analysis(average=False, maximum=False, minimum=False, total=False):
    """Print the chosen statistic of all exposure times."""
    if not observations:
        print("No observation found")
        return

    times = [obs.exposure_seconds for obs in observations]

    if average:
        print(f"Average exposure time is {sum(times) / len(times):.2f} sec")
    if maximum:
        print(f"Maximum exposure time is {max(times)} sec")
    if minimum:
        print(f"Minimum exposure time is {min(times)} sec")
    if total:
        print(f"Total exposure time is {sum(times)} sec")
#---------------------------------------------------------------

def search_observation():
    """Search the observations by target name."""
    if not observations:
        print("No observation found")
        return

    name = input("Target: ").strip().lower()
    found = False

    for obs in observations:
        if obs.target.lower() == name:
            print("\nObservation found")
            print(obs.summary())
            found = True

    if not found:
        print("No target name found")
#---------------------------------------------------------------

def save_to_csv_file():
    """Save all observations into a CSV file."""
    if not observations:
        print("No observation found")
        return

    filename = input("Your file name: ")
    columns = [
        "target", "observer", "filter",
        "exposure_seconds", "apparent_mag", "lambda_nm",
    ]

    with open(f"{filename}.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()

        for obs in observations:
            writer.writerow({
                "target": obs.target,
                "observer": obs.observer,
                "filter": obs.filter_name,
                "exposure_seconds": obs.exposure_seconds,
                "apparent_mag": getattr(obs, "apparent_mag", ""),
                "lambda_nm": getattr(obs, "lambda_nm", ""),
            })
    print("Data saved successfully")


conn = sqlite3.connect("observation.db")
#--------------------------------------------------------------
while True:
    print("=" * 40)
    print()
    print("Welcome to Observer Log".center(40))
    print()
    print("=" * 40)
    print("1. Add Wavelength Observation")
    print("2. Add Brightness Observation")
    print("3. Show Observation")
    print("4. Show Average exposure")
    print("5. Show Maximum exposure")
    print("6. Show Minimum exposure")
    print("7. Show Total exposure")
    print("8. Search target")
    print("9. Save to a csv file")
    print("10. Save to a database")
    print("11. Show bar chart for target vs exposure time")
    print("12. Exit")

#---------------------------------------------------------------

    choice = input("Choose:")

    if choice == "1":
        add_wavelength_observation()
    elif choice == "2":
        add_brightness_observation()
    elif choice == "3":
        show_observation()
    elif choice == "4":
        statistical_analysis(average=True)
    elif choice == "5":
        statistical_analysis(maximum=True)
    elif choice == "6":
        statistical_analysis(minimum=True)
    elif choice == "7":
        statistical_analysis(total=True)
    elif choice == "8":
        search_observation()
    elif choice == "9":
        save_to_csv_file()
    elif choice == "10":
        save_observations_to_db(observations, conn)
    elif choice == "11":
        show_exposure_chart(observations)
    elif choice == "12":
        break
    else:
        print("Please select 1 to 12")

conn.close()







