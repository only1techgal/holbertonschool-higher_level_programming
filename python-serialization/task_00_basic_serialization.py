#!/usr/bin/python3

import json

def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file.
    
    Args:
        data (dict): The Python dictionary to be serialized.
        filename (str): The filename where the JSON data will be saved.
    """
    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
        print(f"Data serialized and saved to '{filename}'.")
    except Exception as e:
        print(f"Error serializing data: {e}")

def load_and_deserialize(filename):
    """Load and deserialize JSON data from a file into a Python dictionary.
    
    Args:
        filename (str): The filename from which to load and deserialize the data.
    
    Returns:
        dict: The deserialized Python dictionary.
    """
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error deserializing data: {e}")
        return None
