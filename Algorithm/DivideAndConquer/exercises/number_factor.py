def number_factor(n):
    if n in [0, 1, 2]:
        return 1
    if n == 3:  # because of the list given.
        return 2
    subtract1 = number_factor(n - 1)
    subtract2 = number_factor(n - 3)
    subtract3 = number_factor(n - 4)
    return subtract1 + subtract2 + subtract3


print(number_factor(5))  # 6
