import typing as t


def bubble_sort(
    arr: list, ordering: t.Literal["asc", "desc"] = "asc"
) -> list:  # O(n^2)
    if ordering == "asc":
        sorted_arr = _asc_bubble_sort(arr)
    else:
        sorted_arr = _desc_bubble_sort(arr)
    return sorted_arr


def _asc_bubble_sort(arr: t.List[int]):
    length = len(arr)
    for i in range(length):  # O(n)
        swapped = False
        not_ordered_last = length - i - 1
        for j in range(0, not_ordered_last):  # O(n)
            swapped = False
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def _desc_bubble_sort(arr: t.List[int]):
    length = len(arr)
    for i in range(length):  # O(n)
        swapped = False
        not_ordered_last = length - i - 1
        for j in range(0, not_ordered_last):  # O(n)
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))
print(bubble_sort(arr, ordering="desc"))
