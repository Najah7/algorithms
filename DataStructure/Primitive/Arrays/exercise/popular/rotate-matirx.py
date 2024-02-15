def rotate(matrix):
    """Rotate a matrix 90 degrees clockwise.
    [1, 2, 3]      [7, 4, 1]
    [4, 5, 6]  ->  [8, 5, 2]
    [7, 8, 9]      [9, 6, 3]

    """

    flatten = [item for row in matrix for item in row]
    flatten.sort(reverse=True)

    rotated_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]

    for col in reversed(range(len(matrix[0]))):
        for row in range(len(matrix)):
            rotated_matrix[row][col] = flatten.pop()

    return rotated_matrix


row1 = range(1, 4)
row2 = range(4, 7)
row3 = range(7, 10)
matrix = [row1, row2, row3]

print(
    "Test for rotate: input=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], output=[[7, 4, 1], [8, 5, 2], [9, 6, 3]]"
)
print(rotate(matrix) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
