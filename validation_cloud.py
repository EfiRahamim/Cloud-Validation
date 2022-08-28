
import csv
import json
import datetime

def val_date(date):
    # printing original string
    print("The original string is : " + str(date))
    # initializing format
    format = "%m/%d/%Y"
    # checking if format matches the date
    res = True
    # using try-except to check for truth value
    try:
        res = bool(datetime.datetime.strptime(date, format))
    except ValueError:
        res = False
        raise ValueError("Incorrect date format should be MM/DD/YYYY or date contains invalid values")

def val_time(time):
    # printing original string
    print("The original string is : " + str(time))
    # initializing format
    format = "%H:%M"
    # checking if format matches the date
    res = True
    # using try-except to check for truth value
    try:
        res = bool(datetime.datetime.strptime(time, format))
    except ValueError:
        res = False
        raise ValueError("Incorrect time format should be hh:mm or time contains invalid values")

def validate_data(data):
    for date in data["Date"]:
        val_date(date)

    # check for commas and replace if there are any
    for i,chip in enumerate(data["Chip"]):
        if "," in str(chip):
            data["Chip"][i] = chip.replace(",", " ")

    kind = "Trappings"  # can also be observations
    if kind == "Trappings":
        for i, title in enumerate(data):
            if i == 6 and title != "Site":
                print("Seventh column should be Site")
    else: # observations
        for i, title in enumerate(data):
            if i == 0 and title != "Site":
                print("first column should be Site")

    # check for valid time, both format and logical
    for time in data["Time"]:
        if time:
            val_time(time)

    print("Done")

def main():

    jsonFile = open("Trappings - test (1).json", "r")
    data = json.load(jsonFile)
    data["Chip"][0] = str(data["Chip"][0]) + ",651351633"
    data["Time"][0] = "12:35"
    print(data)
    jsonFile.close()

