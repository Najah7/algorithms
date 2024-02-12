def extract_diagonal(matrix):
    return [matrix[i][i] for i in range(len(matrix))]


matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print(extract_diagonal(matrix) == [1, 5, 9])
