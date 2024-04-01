def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    
    diag1 = 0
    diag2 = 0

    i = 0
    j = len(matrix) - 1

    while (i<len(matrix)):
        diag1 += matrix[i][i]
        diag2 += matrix[i][j]
        i += 1
        j -= 1

    return diag1 + diag2