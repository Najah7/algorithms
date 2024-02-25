import typing as t


def merge_sort(
    arr: t.List[int], ordering: t.Literal["asc", "desc"] = "asc"
) -> t.List[int]:
    if ordering == "asc":
        return _asc_merge_sort(arr)
    else:  # desc
        return _desc_merge_sort(arr)


def _asc_merge_sort(arr: t.List[int]) -> t.List[int]:  # O(n log n)
    if len(arr) <= 1:  # base case.
        return arr

    # split
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # divide
    sorted_left = _asc_merge_sort(left)  # O(log n)
    sorted_right = _asc_merge_sort(right)  # O(log n)
    # merge
    merged_arr = _asc_merge(arr, sorted_left, sorted_right)  # O(n)
    return merged_arr


def _asc_merge(
    arr: t.List[int], left: t.List[int], right: t.List[int]
) -> t.List[int]:  # O(n)
    merged_arr = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(
        right
    ):  # when both left and right have elements. O(n+m)
        if left[left_idx] < right[right_idx]:
            merged_arr.append(left[left_idx])
            left_idx += 1
        else:
            merged_arr.append(right[right_idx])
            right_idx += 1
    if left_idx < len(left):  # when right is empty
        merged_arr.extend(left[left_idx:])
    if right_idx < len(right):  # when left is empty
        merged_arr.extend(right[right_idx:])
    return merged_arr


def _desc_merge_sort(arr: t.List[int]) -> t.List[int]:  # O(n log n)
    if len(arr) <= 1:  # base case.
        return arr

    # split
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # divide
    sorted_left = _desc_merge_sort(left)  # O(log n)
    sorted_right = _desc_merge_sort(right)  # O(log n)
    # merge
    merged_arr = _desc_merge(arr, sorted_left, sorted_right)  # O(n)
    return merged_arr


def _desc_merge(
    arr: t.List[int], left: t.List[int], right: t.List[int]
) -> t.List[int]:  # O(n)
    merged_arr = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(
        right
    ):  # when both left and right have elements. O(n+m)
        if left[left_idx] > right[right_idx]:
            merged_arr.append(left[left_idx])
            left_idx += 1
        else:
            merged_arr.append(right[right_idx])
            right_idx += 1
    if left_idx < len(left):  # when right is empty
        merged_arr.extend(left[left_idx:])
    if right_idx < len(right):  # when left is empty
        merged_arr.extend(right[right_idx:])
    return merged_arr


arr = [3, 5, 2, 9, 10, 14, 4, 8]
print(merge_sort(arr))
print(merge_sort(arr, ordering="desc"))
