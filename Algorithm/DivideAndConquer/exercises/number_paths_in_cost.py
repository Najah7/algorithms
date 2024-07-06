"""
Number of paths to reach the goal with given cost
"""


def find_paths(maze, row, col, cost):
    if row == -1 or col == -1:
        return 0
    if row == 0 and col == 0:
        return 1 if cost - maze[row][col] == 0 else 0
    go_up = find_paths(maze, row - 1, col, cost - maze[row][col])
    go_left = find_paths(maze, row, col - 1, cost - maze[row][col])
    return go_up + go_left


cost = 25

maze = [[4, 7, 1, 6], [5, 7, 3, 9], [3, 2, 1, 2], [7, 1, 6, 3]]

print(find_paths(maze, 3, 3, cost))  # 2
