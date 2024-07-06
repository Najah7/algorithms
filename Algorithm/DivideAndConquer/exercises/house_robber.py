"""
N: nuber of houses along the street with some amount of money
- Adjacent houses cannot be robbed
- find the maximum amount of money you can rob tonight without alerting the police

we have two options to take:
1. Rob the current house and skip the next house
2. Skip the current house and rob the next house

"""


def find_max_house(houses, current_house):
    if current_house >= len(houses):
        return 0
    # rob the current house
    rob_current = houses[current_house] + find_max_house(houses, current_house + 2)
    # skip the current house
    skip_current = find_max_house(houses, current_house + 1)
    return max(rob_current, skip_current)


houses = [6, 7, 1, 30, 8, 2, 4]
print(find_max_house(houses, 0))  # 7 + 30 + 4 = 41
