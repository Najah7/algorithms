import typing as t

from typing_extensions import Literal

index = int
no_index = Literal[-1]


class BinaryTree:
    """NOTE: array is 1-indexed. 0th index is not used."""

    def __init__(self, size) -> None:
        self.array_size = size
        self.array = [None] * (size + 1)
        self.last_used_index = 0

    def insert_node(self, data) -> None:  # O(1)
        if self.last_used_index + 1 == self.array_size:
            raise Exception("Tree is full")

        self.array[self.last_used_index + 1] = data
        self.last_used_index += 1

    def search_node(self, data) -> t.Union[index, no_index]:  # O(n)
        for i in range(1, self.array_size):  # O(n)
            if self.array[i] == data:
                return i
        return -1

    def pre_order_traversal(self, index) -> None:  # O(n)
        if index > self.last_used_index:
            return

        print(self.array[index], end="->")
        self.pre_order_traversal(index * 2)  # O(n/2)
        self.pre_order_traversal(index * 2 + 1)  # O(n/2)

    def in_order_traversal(self, index) -> None:  # O(n)
        if index > self.last_used_index:
            return

        self.in_order_traversal(index * 2)  # O(n/2)
        print(self.array[index], end="->")
        self.in_order_traversal(index * 2 + 1)  # O(n/2)

    def post_order_traversal(self, index) -> None:  # O(n)
        if index > self.last_used_index:
            return

        self.post_order_traversal(index * 2)  # O(n/2)
        self.post_order_traversal(index * 2 + 1)  # O(n/2)
        print(self.array[index], end="->")

    def level_order_traversal(self) -> None:  # O(n)
        for i in range(1, self.last_used_index + 1):  # O(n)
            print(self.array[i], end="->")

    def delete_node(self, target) -> None:  # O(n)
        if self.last_used_index == 0:
            raise Exception("Tree is empty")

        for i in range(1, self.last_used_index + 1):  # O(n)
            if self.array[i] == target:
                self.array[i] = self.array[self.last_used_index]
                self.array[self.last_used_index] = None
                self.last_used_index -= 1
                return

    def clear(self) -> None:  # O(1)
        self.array = None
        self.last_used_index = 0


def sample_BT() -> BinaryTree:
    BT = BinaryTree(10)
    BT.insert_node("Root")
    BT.insert_node("Left")
    BT.insert_node("Right")
    BT.insert_node("Left/Left")
    BT.insert_node("Left/Right")
    BT.insert_node("Right/Left")
    BT.insert_node("Right/Right")

    return BT


BT = sample_BT()
BT.pre_order_traversal(1)  # O(n)
print()
BT.in_order_traversal(1)  # O(n)
print()
BT.post_order_traversal(1)  # O(n)
print()
BT.level_order_traversal()  # O(n)
