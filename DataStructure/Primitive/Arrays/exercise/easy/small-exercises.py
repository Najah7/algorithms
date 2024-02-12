def max_product(arr):
    arr.sort(reverse=True)
    return arr[0] * arr[1]


print("Test for max_product: input=[1, 2, 3, 4, 6], output=24")
print(max_product([1, 2, 3, 4, 6]) == 24)


def middle(arr):
    length = len(arr)
    mid = length // 2
    if length % 2 == 0:
        return arr[mid - 1 : mid + 1]
    else:
        return arr[mid]


print("Test for middle: input=[1, 2, 3, 4, 6], output=[3]")
print(middle([1, 2, 3, 4, 6]) == 3)
print("Test for middle: input=[1, 2, 3, 4, 6, 7], output=[3, 4]")
print(middle([1, 2, 3, 4, 6, 7]) == [3, 4])


def diagonal_sum(matrix):
    total = 0
    for i, row in enumerate(matrix):
        total += row[i]
    return total


print("Test for diagonal_sum: input=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], output=15")
print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 15)


def first_second(arr):
    arr.sort(reverse=True)
    return arr[0], arr[1]


def remove_duplicates(arr):
    return list(set(arr))


print(
    "Test for remove_duplicates: input=[1, 2, 3, 4, 6, 7, 7, 7, 7], output=[1, 2, 3, 4, 6, 7]"
)
print(remove_duplicates([1, 2, 3, 4, 6, 7, 7, 7, 7]) == [1, 2, 3, 4, 6, 7])


def pair_sum(myList, sum_value):
    completements = {}
    pairs = []

    for num in myList:
        if num in completements:
            pairs.append([num, completements[num]])
        completements[sum_value - num] = num

    return pairs


print("Test for pair_sum: input=[1, 2, 3, 4, 6, 7], output=[[1, 6], [2, 5], [3, 4]]")
print(pair_sum([1, 2, 3, 4, 6, 7], 7) == [[4, 3], [6, 1]])


def contains_duplicate(nums):
    if len(nums) != len(set(nums)):
        return True
    return False


print("Test for contains_duplicate: input=[1, 2, 3, 4, 6, 7], output=False")
print(contains_duplicate([1, 2, 3, 4, 6, 7]) == False)
print("Test for contains_duplicate: input=[1, 2, 3, 4, 6, 7, 7], output=True")
print(contains_duplicate([1, 2, 3, 4, 6, 7, 7]) == True)
