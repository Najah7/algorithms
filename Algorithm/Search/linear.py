def linear_search(array, target): # O(n)
    for i, item in enumerate(array):  # O(n)
        if item == target:
            return i
    return -1
