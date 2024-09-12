#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Computes the square value of integers of a matrix
    # Returns a new matrix of the same size.
    return [[x ** 2 for x in row] for row in matrix]
