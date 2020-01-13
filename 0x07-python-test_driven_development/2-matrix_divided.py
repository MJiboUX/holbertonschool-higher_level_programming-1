#!/usr/bin/python3
"""
   Program that divides all elements of a matrix
"""
def matrix_divided(matrix, div):
    """Function to devide the matrix
       Args:
           matrix: multi-dimensional list
           div: list divisor
       Returns:
           The new divided matrix.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(x, list) for x in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for x in matrix:
        if len(x) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[x / div for x in row] for row in matrix]
    new_matrix = [[round(x,2) for x in row] for row in new_matrix]
    return(new_matrix)
