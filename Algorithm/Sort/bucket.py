import math
import typing as t

from insertion import insert_sort


def bucket_sort(
    arr: t.List[int], ordering: t.Literal["asc", "desc"] = "asc"
) -> t.List[int]:  # O(n log n)
    if ordering == "asc":
        sorted_arr = _asc_bucket_sort(arr)
    else:  # desc
        sorted_arr = _desc_bucket_sort(arr)
    return sorted_arr


def _asc_bucket_sort(arr: t.List[int]) -> t.List[int]:  # O(n log n)
    max_elem = max(arr)
    min_elem = min(arr)
    range_val = max_elem - min_elem
    # prepare buckets
    num_buckets = round(math.sqrt(len(arr)))
    buckets = [[] for _ in range(num_buckets)]  # O(sqrt(n)) -> O(n)

    for elem in arr:
        if range_val == 0:
            bucket_index = 0
        else:
            normalized_elem = (elem - min_elem) / range_val
            max_index = num_buckets - 1
            bucket_index = math.floor(normalized_elem * max_index)

        buckets[bucket_index].append(elem)

    for i in range(num_buckets):  # O(sqrt(n)) -> O(n)
        buckets[i] = insert_sort(buckets[i])  # O(num_bucket^2) -> O(log n)

    return [elem for bucket in buckets for elem in bucket]


def _desc_bucket_sort(arr: t.List[int]) -> t.List[int]:  # O(n log n)
    max_elem = max(arr)
    min_elem = min(arr)
    range_val = max_elem - min_elem
    # prepare buckets
    num_buckets = round(math.sqrt(len(arr)))
    buckets = [[] for _ in range(num_buckets)]  # O(sqrt(n)) -> O(n)

    for elem in arr:
        if range_val == 0:
            bucket_index = 0
        else:
            normalized_elem = (elem - min_elem) / range_val
            max_index = num_buckets - 1
            bucket_index = math.floor(normalized_elem * max_index)

        buckets[bucket_index].append(elem)

    for i in range(num_buckets):  # O(sqrt(n)) -> O(n)
        buckets[i] = insert_sort(
            buckets[i], ordering="desc"
        )  # O(num_bucket^2) -> O(log n)

    return [elem for bucket in buckets for elem in bucket]


arr = [64, 34, 25, 12, 22, 11, 90]
print(bucket_sort(arr))
print(bucket_sort(arr, ordering="desc"))
