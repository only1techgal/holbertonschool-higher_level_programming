#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Use " ".join to format the row correctly with spaces between elements
        print(" ".join("{:d}".format(element) for element in row))
