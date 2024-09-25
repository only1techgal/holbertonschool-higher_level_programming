#!/usr/bin/python3

from abc import ABC, abstractmethod


# Abstract base class Animal
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


# Dog class inheriting from Animal
class Dog(Animal):
    def sound(self):
        return "Bark"  # This line should be indented with 4 spaces


# Cat class inheriting from Animal
class Cat(Animal):
    def sound(self):
        return "Meow"
