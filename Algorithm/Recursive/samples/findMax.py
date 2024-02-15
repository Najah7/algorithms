def find_max_recursion(arr, n):  # a + M(n-a) -> O(n)
    if n == 1:
        return arr[0]
    else:
        index = n - 1
        return max(arr[index], find_max_recursion(arr, n - 1))  # O(n) + M(n-1)


def find_max(arr):
    return find_max_recursion(arr, len(arr))


print(find_max([1, 4, 8, 3, 0, 2]) == 8)
