#!/usr/bin/python3

class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        item = next(self.iterator)  # Fetch the next item
        self.counter += 1           # Increment the counter
        return item

    def get_count(self):
        return self.counter
