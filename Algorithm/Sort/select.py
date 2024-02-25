import typing as t


def select_sort(
    arr: t.List[int], ordering: t.Literal["asc", "desc"] = "asc"
) -> t.List[int]:  # O(n^2)
    if ordering == "asc":
        sorted_arr = _asc_select_sort(arr)
    else:  # desc
        sorted_arr = _desc_select_sort(arr)
    return sorted_arr


def _asc_select_sort(arr: t.List[int]) -> t.List[int]:
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def _desc_select_sort(arr: t.List[int]) -> t.List[int]:
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print(select_sort(arr))
print(select_sort(arr, ordering="desc"))
