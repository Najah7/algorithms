class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class LLStack:
    class StackEmptyError(Exception):
        def __init__(self) -> None:
            super().__init__("Stack is Empty")

    def __init__(self) -> None:
        self.items = LinkedList()
        self.length = 0

    def is_empty(self) -> bool:
        if self.items.head is None:
            return True
        return False

    def push(self, value) -> None:
        new_node = Node(value)
        new_node.next = self.items.head
        self.items.head = new_node

    def pop(self) -> Node:
        if self.is_empty():
            raise self.StackEmptyError
        else:
            poped_node = self.items.head
            self.items.head = self.items.head.next
            return poped_node

    def peek(self) -> Node:
        if self.is_empty():
            raise self.StackEmptyError
        else:
            return self.items.head

    def clear(self):
        self.items.head = None
