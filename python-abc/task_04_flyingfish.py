#!/usr/bin/python3

class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()     # Output: The flying fish is swimming!
    flying_fish.fly()      # Output: The flying fish is soaring!
    flying_fish.habitat()  # Output: The flying fish lives in water/sky!

    print(FlyingFish.mro())  # Prints the method resolution order
