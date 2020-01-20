#!/usr/bin/python3
"""
Matrix multiplication
"""
def matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices
       Args:
           m_a: matrix a
           m_b: matrix b
       Returns: new matrix.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    elem = [[]]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                elem[i][j] += m_a[i][j] * m_b[k][j]
    return(elem)
