class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class CircularDoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        # when the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
        # when the list is not empty
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, value):
        new_node = Node(value)
        # when the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
        # when the list is not empty
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head = new_node
        self.size += 1

    def insert(self, index, value):
        if not (0 <= index <= self.size):
            raise IndexError("Index out of range")
        if self.head is None:
            raise ValueError("List is empty")

        if index == 0:
            self.prepend(value)
            return
        elif index == self.size:
            self.append(value)
            return
        else:
            new_node = Node(value)
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.prev = current_node
            new_node.next = current_node.next
            current_node.next.prev = new_node
            current_node.next = new_node
            self.size += 1

    def find(self, value):
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.value == value:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break

    def remove(self, index):
        if not (0 <= index < self.size):
            raise IndexError("Index out of range")

        if self.head is None:
            raise ValueError("List is empty")

        if index == 0:  # first node
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            self.size -= 1
            return
        elif index == self.size - 1:  # last node
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            self.size -= 1
            return
        else:  # middle node
            current_node = self.head
            # move to the node to be removed
            for _ in range(index):
                current_node = current_node.next
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            self.size -= 1
            return

    def clear(self):
        if self.head is None:
            return

        self.tail.next = None
        current_node = self.head
        while current_node is not None:
            current_node.prev = None
            current_node = current_node.next
        self.head = None
        self.tail = None

    def __str__(self):
        nodes = [str(node) for node in self]
        return " <-> ".join(nodes)

    def __repr__(self) -> str:
        self.__str__()

    def __len__(self):
        return self.size

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next
            if current_node == self.head:
                break
        return

    def __reversed__(self):
        if self.head is None:
            return

        current_node = self.tail
        while current_node is not None:
            yield current_node
            current_node = current_node.prev
            if current_node == self.tail:
                break

    def __getitem__(self, index):
        if index >= self.size:
            raise IndexError("Index out of range")
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.value

    def __setitem__(self, index, value):
        if index >= self.size:
            raise IndexError("Index out of range")
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        current_node.value = value

    def __delitem__(self, index):
        if index >= self.size:
            raise IndexError("Index out of range")
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        self.remove(index)
