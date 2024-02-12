class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.size = 0
        if value is not None:
            self.append(value)

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def generate(self, *args):
        for value in args:
            self.add(value)

    def generate_between(self, start, end):
        for i in range(start, end):
            self.add(i)

    def generate_random(self, length, min=0, max=100):
        from random import randint

        for _ in range(length):
            self.add(randint(min, max))

    def __inter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __str__(self) -> str:
        return " <-> ".join([str(node) for node in self])

    def __len__(self):
        return self.size
