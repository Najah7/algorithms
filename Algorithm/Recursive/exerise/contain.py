def contain(arr, condition_callback):
    if len(arr) == 0:
        return False

    if not (condition_callback(arr[0])):
        return contain(arr[1:], condition_callback)
    return True


def is_odd(num):
    if num % 2 == 0:
        return False
    return True


print(contain([1, 2, 3, 4, 5], is_odd) == True)
print(contain([2, 4, 6, 8, 10], is_odd) == False)
