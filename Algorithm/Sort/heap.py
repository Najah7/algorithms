import typing as t


class Heap:
    def __init__(
        self, arr: t.List[int], ordering: t.Literal["asc", "desc"] = "asc"
    ) -> None:
        self.arr = []
        self.ordering = ordering
        self.size = 0
        for elem in arr:  # O(n)
            self.insert(elem)

    class HeapEmptyError(Exception):
        def __init__(
            self,
        ) -> None:
            super().__init__("Heap is empty.")

    def insert(self, val: int) -> None:
        self.arr.append(val)
        self.size += 1
        self._heapify()

    def pop(self) -> int:
        if not self.arr:
            raise self.HeapEmptyError
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        val = self.arr.pop()
        self.size -= 1
        self._heapify()  # O(log n)
        return val

    def _heapify(self) -> None:  # O(n log n)
        last_parent = self.size // 2 - 1
        for node_index in range(last_parent, -1, -1):  # O(n/2) -> O(n)
            self._heapify_down(node_index)  # O(log n)

    def _heapify_down(self, idx: int) -> None:  # O(log n)
        if self.ordering == "asc":
            self._asc_heapify_down(idx)  # O(log n)
        else:  # desc
            self._desc_heapify_down(idx)  # O(log n)

    def _asc_heapify_down(
        self, idx: int
    ) -> None:  # O(log n) (most of the time: O(1) (just one swap))
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if (
            left < self.size and self.arr[left] < self.arr[smallest]
        ):  # when left child is smaller than parent
            smallest = left

        if (
            right < self.size and self.arr[right] < self.arr[smallest]
        ):  # when right child is smaller than parent
            smallest = right

        if (
            smallest != idx
        ):  # if parent is not the smallest and swap and then heapify down again
            self.arr[idx], self.arr[smallest] = self.arr[smallest], self.arr[idx]
            self._asc_heapify_down(smallest)  # O(log n)

    def _desc_heapify_down(
        self, i: int
    ) -> None:  # O(log n) (most of the time: O(1) (just one swap))
        biggest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if (
            left < self.size and self.arr[left] > self.arr[biggest]
        ):  # when left child is bigger than parent
            biggest = left
        if (
            right < self.size and self.arr[right] > self.arr[biggest]
        ):  # when right child is bigger than parent
            biggest = right
        if (
            biggest != i
        ):  # if parent is not the biggest and swap and then heapify down again
            self.arr[i], self.arr[biggest] = self.arr[biggest], self.arr[i]
            self._desc_heapify_down(biggest)  # O(log n)


def heap_sort(
    arr: t.List[int], ordering: t.Literal["asc", "desc"] = "asc"
) -> t.List[int]:  # O(n log n)
    if ordering == "asc":
        sorted_arr = []
        heap = Heap(arr)  # O(n)
        for _ in range(heap.size):
            sorted_arr.append(heap.pop())
        return sorted_arr
    else:  # desc
        sorted_arr = []
        heap = Heap(arr, ordering="desc")  # O(n)
        for _ in range(heap.size):
            sorted_arr.append(heap.pop())
        return sorted_arr


arr = [3, 2, 1, 5, 4]
print(heap_sort(arr))  # [1, 2, 3, 4, 5]
print(heap_sort(arr, ordering="desc"))  # [5, 4, 3, 2, 1]
