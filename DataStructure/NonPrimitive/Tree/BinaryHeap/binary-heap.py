import typing as t

HeapType = t.Literal["Min", "Max"]


class BinaryHeap:
    class HeapEmptyError(Exception):
        def __init__(self) -> None:
            super().__init__("Heap is empty")

    class HeapFullError(Exception):
        def __init__(self) -> None:
            super().__init__("Heap is full")

    class HeapTypeError(Exception):
        def __init__(self) -> None:
            super().__init__("You must select the type of the heap")

    def __init__(self, size: int, type: HeapType) -> None:
        self.array: t.List[int, None] = [None] * (size + 1)
        self.type: HeapType = type
        self.size: int = 0
        self.max_size: int = size

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    def peek(self) -> int:  # O(1)
        if self.is_empty:
            raise self.HeapEmptyError
        return self.array[1]

    def level_order(self) -> None:  # O(n)
        if self.is_empty:
            raise self.HeapEmptyError

        for i in range(1, self.size + 1):
            print(self.array[i], end=" ")

    def insert(self, value: int) -> None:  # O(log n)
        if self.size == self.max_size:
            raise self.HeapFullError

        # add the value to the end of the array
        self.size += 1
        self.array[self.size] = value
        i = self.size

        # move the value up to its correct position
        if self.type == "Max":
            while 1 < i and self.array[i // 2] < value:  # O(log n)
                self.array[i] = self.array[i // 2]
                i = i // 2
        elif self.type == "Min":
            while 1 < i and value < self.array[i // 2]:  # O(log n)
                self.array[i] = self.array[i // 2]
                i = i // 2

        self.array[i] = value

    def pop(self) -> int:  # O(log n)
        if self.is_empty:
            raise self.HeapEmptyError

        # save the value to be returned
        retval = self.array[1]

        # move the last value to the root
        self.array[1] = self.array[self.size]
        self.size -= 1

        # move the value down to its correct position
        if self.type == "Max":
            i = 1
            while 2 * i <= self.size:  # O(log n)
                child = 2 * i
                if (
                    child + 1 <= self.size and self.array[child] < self.array[child + 1]
                ):  # select the larger child (left/right)
                    child += 1
                if (
                    self.array[i] < self.array[child]
                ):  # if the child is larger than the parent, swap them
                    self.array[i], self.array[child] = self.array[child], self.array[i]
                    i = child
                else:
                    break
        elif self.type == "Min":
            i = 1
            while 2 * i <= self.size:  # O(log n)
                child = 2 * i
                if (
                    child + 1 <= self.size and self.array[child + 1] < self.array[child]
                ):  # select the smaller child (left/right)
                    child += 1
                if (
                    self.array[child] < self.array[i]
                ):  # if the child is smaller than the parent, swap them
                    self.array[i], self.array[child] = self.array[child], self.array[i]
                    i = child
                else:
                    break

        return retval

    def clear(self) -> None:  # O(1)
        self.array = [None] * (self.max_size + 1)
        self.size = 0


binary_heap = BinaryHeap(10, "Min")
binary_heap.insert(2)
binary_heap.insert(17)
binary_heap.insert(3)
binary_heap.insert(19)
binary_heap.insert(1)
binary_heap.level_order()
print()
binary_heap.pop()
binary_heap.clear()
binary_heap.insert(2)
binary_heap.level_order()
