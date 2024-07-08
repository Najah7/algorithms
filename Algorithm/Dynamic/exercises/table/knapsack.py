#NOTE: zero one knapsack

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def knapsack_table(items, capacity):
    # for padding
    items = [Item(0, 0)] + items

    # initialize the table with zeros. x: items, y: capacity
    table = [[0] * (capacity + 1) for _ in range(len(items))]

    # calculate the maximum value
    for i in range(1, len(items)):
        # i: item index, j: capacity
        for j in range(1, capacity + 1):
            if items[i].weight > j:
                table[i][j] = table[i - 1][j]
            else:
                take = items[i].value + table[i - 1][j - items[i].weight]
                leave = table[i - 1][j]
                table[i][j] = max(take, leave)

    return table[len(items) - 1][capacity]

items = [Item(3, 31), Item(1, 26), Item(2, 17), Item(5, 72)]

print(knapsack_table(items, 7))  # 98
