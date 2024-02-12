import numpy as np

matrix = [[1, 2, 3], [4, 5, 6]]

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end=" ")
    print()

# add a new row (append to the end)
matrix.append([7, 8, 9])  # O(1)
print(matrix)

# add a new row (insert at the beginning)
matrix.insert(0, [-2, -1, 0])  # O(n) (insert: O(1), shift: O(n))

# add a new column(insert at the beginning)

# from scratch
new_col = [10] * len(matrix)

new_matrix = np.zeros((len(matrix), len(matrix[0]) + 1), dtype=int)

# shift all the elements to the right
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        new_matrix[row][col + 1] = matrix[row][col]  # O(n^2)

for index, col in enumerate(new_col):
    new_matrix[index][0] = col  # O(n)

# useful numpy function
new_matrix2 = np.insert(matrix, 0, new_col, axis=1)  # O(n^2)

print(new_matrix)
print(new_matrix2)

print((new_matrix == new_matrix2).all())

# delete a row
matrix.pop()  # O(1)
print(matrix)

# delete a column
for row in range(len(matrix)):
    matrix[row].pop(0)  # O(n)
