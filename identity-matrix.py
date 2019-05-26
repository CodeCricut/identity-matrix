def is_identity_matrix(matrix):
    n = len(matrix)
    if len(matrix[0]) != n:
        return False
    r = 0
    c = 0
    while r < n:
        c = 0
        while c < n:
            if matrix[r][r] != 1:
                return False
            if r != c:
                if matrix[r][c] != 0:
                    return False
            c += 1
        r += 1
    return True


# Test Cases:

matrix1 = [[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]
print(is_identity_matrix(matrix1))
# >>>True

matrix2 = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]

print(is_identity_matrix(matrix2))
# >>>False

matrix3 = [[2, 0, 0],
           [0, 2, 0],
           [0, 0, 2]]

print(is_identity_matrix(matrix3))
#>>>False