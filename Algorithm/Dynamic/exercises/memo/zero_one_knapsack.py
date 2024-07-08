class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def zero_one_knapsack(items, capacity, currentIndex, tempDict):
    key = str(currentIndex) + str(capacity)

    if key in tempDict:
        return tempDict[key]
    
    if capacity <=0:
        return 0
        
    if  not (0 <= currentIndex < len(items)):
        return 0

    if capacity < items[currentIndex].weight:
        return zero_one_knapsack(items, capacity, currentIndex + 1, tempDict)
    
    take = items[currentIndex].profit + zero_one_knapsack(items, capacity-items[currentIndex].weight, currentIndex+1, tempDict)
    leave = zero_one_knapsack(items, capacity, currentIndex + 1, tempDict)
    tempDict[key] = max(take, leave)
    return tempDict[key]

items = [Item(31, 3), Item(26, 1), Item(17, 2), Item(72, 5)]
print(zero_one_knapsack(items, 7, 0, {}))  # 98