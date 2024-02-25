import random
import typing as t


def quick_sort(
    arr: t.List[int], ordering: t.Literal["asc", "desc"] = "asc"
) -> t.List[int]:  # O(n log n)
    if ordering == "asc":
        return _asc_quick_sort(arr)
    else:  # desc
        return _desc_quick_sort(arr)


def _calc_pivot(
    arr: t.List[int], method: t.Literal["first", "random", "three median"]
) -> int:
    if method == "first":
        return arr[0]
    if method == "random":
        return arr[random.randint(0, len(arr) - 1)]
    if method == "three median":
        first = arr[0]
        mid = arr[len(arr) // 2]
        last = arr[-1]
        if first < mid < last or last < mid < first:
            return mid
        if mid < first < last or last < first < mid:
            return first
        return last


def _asc_quick_sort(arr: t.List[int]) -> t.List[int]:  # O(n log n)
    if len(arr) <= 1:  # base case.
        return arr

    pivot = _calc_pivot(arr, "three median")
    swap = 0
    for i in range(len(arr)):  # O(n)
        if arr[i] < pivot:
            arr[i], arr[swap] = arr[swap], arr[i]
            swap += 1
    return (
        _asc_quick_sort(arr[:swap]) + [pivot] + _asc_quick_sort(arr[swap + 1 :])
    )  # O(log n)


def _desc_quick_sort(arr: t.List[int]) -> t.List[int]:  # O(n log n)
    if len(arr) <= 1:  # base case.
        return arr

    pivot = _calc_pivot(arr, "three median")
    swap = 0
    for i in range(len(arr)):
        if arr[i] > pivot:
            arr[i], arr[swap] = arr[swap], arr[i]
            swap += 1
    return _desc_quick_sort(arr[:swap]) + [pivot] + _desc_quick_sort(arr[swap + 1 :])


arr = [3, 2, 1, 5, 4]
print(quick_sort(arr))
print(quick_sort(arr, ordering="desc"))
