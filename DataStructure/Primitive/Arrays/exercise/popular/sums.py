"""
Check points
- Does array contain only positive integers or negative integers or both?
- What if the same pair repeats twice, should we print every pair?
- If the reverse of the pair is acceptable?
- Do we need to print only distinct pairs?
- How big is the array?
"""


# case: just for pairs
def two_sum(arr, target):
    seen = {}

    for i, num in enumerate(arr):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i


print("Test for two_sum: input=[2, 7, 11, 15], target=9, output=[0, 1]")
print(two_sum([2, 7, 11, 15], 9) == [0, 1])


# codes below are solved by Dynamic Programming
def sum_comb(arr, target):
    dp = [[]] * (target + 1)

    for i in range(1, target + 1):
        for num in arr:
            if num <= i:
                if i - num == 0:
                    dp[i] = [num]
                elif dp[i - num]:
                    dp[i] = dp[i - num] + [num]

    return dp[target]


def sum_comb_index(arr, target):
    dp = [[]] * (target + 1)

    for i in range(1, target + 1):
        for num in arr:
            if num <= i:
                if i - num == 0:
                    dp[i] = [arr.index(num)]
                elif dp[i - num]:  # if dp[i - num] is not empty
                    dp[i] = dp[i - num] + [arr.index(num)]

    return dp[target]


print("Test for sum_comb: input=[2, 7, 11, 15], target=9, output=[2, 7]")
print(sum_comb([2, 7, 11, 15], 9) == [2, 7])
print("Test for sum_comb_indices: input=[2, 7, 11, 15], target=9, output=[0, 1]")
print(sum_comb_index([2, 7, 11, 15], 9) == [0, 1])
