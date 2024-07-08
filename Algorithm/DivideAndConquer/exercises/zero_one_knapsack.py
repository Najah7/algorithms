"""
Zero One Knapsack Problem

- N: number of items
- V: value of items
- C: capacity of knapsack
- W: weight of items

find the maximum value that can be put into the knapsack

we have two options for each item:
- take it: c + f(i + 1, c - w[i])
- leave it: 0 + f(i + 1, c)
"""

import typing as t


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def zo_knapsack(items: t.List[Item], capacity: int, i: int):
    if i == len(items):
        return 0
    if items[i].weight > capacity:
        return zo_knapsack(items, capacity, i + 1)
    take = items[i].value + zo_knapsack(items, capacity - items[i].weight, i + 1)
    leave = zo_knapsack(items, capacity, i + 1)
    return max(take, leave)

def zo_knapsack_with_memo(items: t.List[Item], capacity: int, i: int, memo: t.Dict[t.Tuple[int, int], int]):
    if i == len(items):
        return 0
    if items[i].weight > capacity:
        return zo_knapsack_with_memo(items, capacity, i + 1, memo)
    if (i, capacity) in memo:
        return memo[(i, capacity)]
    take = items[i].value + zo_knapsack_with_memo(items, capacity - items[i].weight, i + 1, memo)
    leave = zo_knapsack_with_memo(items, capacity, i + 1, memo)
    memo[(i, capacity)] = max(take, leave)
    return memo[(i, capacity)]


capacity = 10

items = [Item(1, 5), Item(2, 4), Item(3, 3), Item(4, 2), Item(5, 1)]

print(zo_knapsack(items, capacity, 0))  # 14