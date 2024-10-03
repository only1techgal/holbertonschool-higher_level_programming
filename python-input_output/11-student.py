#!/usr/bin/python3

"""
This module defines a student class with attributes and methods for
serialization and deserialization of student instances
"""


class Student:
    """
    Represents  student with first name, last name, and age
    """

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }

        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):

        for key, value in json.items():
            setattr(self, key, value)
