# from scratch
def reverse(arr):
    for i in range(len(arr) // 2):
        # NOTE: you can use temp variable to store the value
        arr[i], arr[-i - 1] = arr[-i - 1], arr[i]
