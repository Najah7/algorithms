class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class CircularSingleLinkedList:
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
            self.tail.next = self.head
        # when the list is not empty
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.size += 1

    def prepend(self, value):
        new_node = Node(value)
        # when the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        # when the list is not empty
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.size += 1

    def insert(self, index, value):
        if not (0 <= index <= self.size):
            raise IndexError("Index out of range")
        new_node = Node(value)
        current_node = self.head
        previous_node = self.tail
        # move to the node before the index
        for _ in range(index - 1):
            current_node = current_node.next
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = current_node.next
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
            if current_node == self.head:
                break
        return -1

    def pop(self):
        # when the list is empty
        if self.head is None:
            return
        # when the list has only one node
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        # when the list has more than one node
        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next
        current_node.next = self.head
        self.tail = current_node
        self.size -= 1

    def pop_first(self):
        # when the list is empty
        if self.head is None:
            return
        # when the list has only one node
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:  # when the list has more than one node
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1

    def get(self, index):
        if not (0 <= index < self.size):
            raise IndexError("Index out of range")
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

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

        current_node = self.head
        previous_node = self.tail
        # move to the node to be removed
        for _ in range(index - 1):
            previous_node = current_node
            current_node = current_node.next
        # previous
        if current_node == self.head:
            self.head = current_node.next
            self.tail.next = self.head
        # next
        else:
            previous_node.next = current_node.next
        self.size -= 1

    def clear(self):
        if self.size == 0:
            return

        self.tail.next = None
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self) -> str:
        result = ""
        current_node = self.head
        while current_node is not None:
            result += str(current_node.value) + " -> "
            current_node = current_node.next
            if current_node == self.head:
                break
        return result + "..."

    def __len__(self):
        return self.size

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next
            if current_node == self.head:
                break

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        self.get(index).value = value
