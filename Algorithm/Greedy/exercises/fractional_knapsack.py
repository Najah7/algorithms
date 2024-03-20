import typing as t


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.normalized_value = value / weight


def fractional_knapsack(items: t.List[Item], capacity: int) -> float:  # O(nlogn)
    items.sort(key=lambda x: x.normalized_value, reverse=True)  # O(nlogn)
    total_value = 0
    for item in items:  # O(n)
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.normalized_value * capacity
            break
    return total_value


item1 = Item(10, 60)
item2 = Item(20, 100)
item3 = Item(30, 120)
items = [item1, item2, item3]
capacity = 50
print(fractional_knapsack(items, capacity))
