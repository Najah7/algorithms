# simple
def missing_num(arr, n):
    for i in range(1, n + 1):
        if i not in arr:
            return i
    return -1


# efficient
# arithmetic series sum: n * (n + 1) / 2
def efficient_missing_num(arr, n):
    total = (n * (n + 1)) // 2
    arr_sum = sum(arr)
    missing = total - arr_sum
    return missing


print("Test 1: input=[1, 2, 3, 4, 6], output=5")
print((missing_num([1, 2, 3, 4, 6], 6) == 5))
print((efficient_missing_num([1, 2, 3, 4, 6], 6) == 5))
