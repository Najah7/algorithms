def binary_search(sorted_arr: list, target: int):  # O(log n)
    left = 0
    right = len(sorted_arr) - 1

    while left <= right:  # O(log n)
        mid = (left + right) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
