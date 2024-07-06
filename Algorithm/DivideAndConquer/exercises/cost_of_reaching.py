"""
Minimum cost to reach the end of the goal

tips:
 think of this problem from the goal to the start


"""


def find_min_cost(maze, row, col):
    if row == -1 or col == -1:  # out of bound
        return float("inf")
    if row == 0 and col == 0:
        return maze[row][col]

    go_up = find_min_cost(maze, row - 1, col)
    go_left = find_min_cost(maze, row, col - 1)

    return maze[row][col] + min(go_up, go_left)


maze = [
    [4, 7, 8, 6, 4],
    [6, 7, 3, 9, 2],
    [3, 8, 1, 2, 4],
    [7, 1, 7, 3, 7],
    [2, 9, 8, 9, 3],
]

print(find_min_cost(maze, 4, 4))  # 36
