#!/usr/bin/python3

"""
This module defines a Student class with attributes and ma method
to retrieve a dictionary representation of the instance
"""


class Student:
    """
    Represents a student with first name, last name, and age
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
