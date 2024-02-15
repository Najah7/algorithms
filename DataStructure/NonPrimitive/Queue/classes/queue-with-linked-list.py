class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next


class LLQueue:
    class QueueEmptyError(Exception):
        def __init__(self) -> None:
            super().__init__("Queue is empty")

    def __init__(self) -> None:
        self.items = LinkedList()

    def __str__(self) -> str:
        str_items = map(str, self.items)
        return " ".join(str_items)

    def enqueu(self, value):
        new_node = Node(value)
        if self.items.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.items.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise self.QueueEmptyError

        dequeued_node = self.items.head
        if self.items.head == self.items.tail:
            self.items.head = None
            self.items.tail = None
        else:
            self.items.head = self.items.head.next
        return dequeued_node

    def peek(self):
        if self.is_empty():
            raise self.QueueEmptyError

        return self.items.head

    def is_empty(self):
        return self.items.head == None

    def clear(self):
        self.items.head = None
        self.items.tail = None
