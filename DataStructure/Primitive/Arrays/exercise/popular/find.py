import numpy as np

nums_within_20 = np.arange(1, 21)


def linear_search(array, target):
    for i, item in enumerate(array):  #! O(n)
        if item == target:  # O(1)
            return i  # O(1)
    return -1  # O(1)


def binary_search(nums, target):
    low = 0  # O(1)
    high = len(nums) - 1  # O(1)

    while low <= high:  #! O(log(n))
        mid = (low + high) // 2  # O(1)
        if nums[mid] == target:  # O(1)
            return mid  # O(1)
        elif nums[mid] > target:  # O(1)
            high = mid - 1  # O(1)
        else:
            low = mid + 1  # O(1)
    return -1  # O(1)
