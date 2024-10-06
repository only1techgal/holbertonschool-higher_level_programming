#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts data from CSV file to JSON format and writes to data.json."""
    try:
        # Open the CSV file and read it using DictReader
        with open(csv_filename, mode='r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # Convert rows into a list of dictionaries
            data = [row for row in csv_reader]

        # Write the list of dictionaries to data.json in JSON format
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
