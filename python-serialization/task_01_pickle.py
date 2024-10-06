#!/usr/bin/python3

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """Initialize the CustomObject with name, age, and is_student."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object and save it to the filename using pickle."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized and saved to {filename}")
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserialize the object from the provided filename."""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                return obj
        except (FileNotFoundError, pickle.PickleError, EOFError) as e:
            print(f"Error deserializing object: {e}")
            return None
