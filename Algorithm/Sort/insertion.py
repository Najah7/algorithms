import typing as t


def insert_sort(
    arr: t.List[int], ordering: t.Literal["asc", "desc"] = "asc"
) -> t.List[int]:  # O(n^2)
    if ordering == "asc":
        sorted_arr = _asc_insert_sort(arr)
    else:
        sorted_arr = _desc_insert_sort(arr)
    return sorted_arr


def _asc_insert_sort(arr: t.List[int]) -> t.List[int]:
    for i in range(1, len(arr)):  # O(n)
        elem = arr[i]
        j = i - 1
        while j >= 0 and elem < arr[j]:  # O(n)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr


def _desc_insert_sort(arr: t.List[int]) -> t.List[int]:
    for i in range(1, len(arr)):  # O(n)
        elem = arr[i]
        j = i - 1
        while j >= 0 and elem > arr[j]:  # O(n)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(insert_sort(arr))
    print(insert_sort(arr, ordering="desc"))
