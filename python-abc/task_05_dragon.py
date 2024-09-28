#!/usr/bin/python3

class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")


if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()  # Output: The creature swims!
    dragon.fly()   # Output: The creature flies!
    dragon.roar()  # Output: The dragon roars!
