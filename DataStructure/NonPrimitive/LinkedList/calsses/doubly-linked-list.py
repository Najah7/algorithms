class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def remove(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                self.size -= 1
                return
            current_node = current_node.next

    def find(self, value):
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.value == value:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def get(self, index):
        if not (0 <= index < self.size):
            raise IndexError("Index out of range")

        mid = self.size // 2

        # when index is closer to the head
        if index < mid:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        # when index is closer to the tail
        else:
            current_node = self.tail
            for _ in range(self.size - index - 1):
                current_node = current_node.prev

        return current_node.value

    def pop(self):
        # when the list is empty
        if self.head is None:
            return
        # when the list has only one element
        if self.size == 1:
            poped_value = self.head.value
            self.head = None
            self.tail = None
            self.size -= 1
            return poped_value

        poped_value = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        return poped_value

    def pop_first(self):
        # when the list is empty
        if self.head is None:
            return
        # when the list has only one element
        if self.size == 1:
            poped_value = self.head.value
            self.head = None
            self.tail = None
            self.size -= 1
            return poped_value

        poped_value = self.head.value
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        return poped_value

    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def insert(self, index, value):
        if not (0 <= index <= self.size):
            raise IndexError("Index out of range")
        new_node = Node(value)
        # when the list is empty
        if index == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        # when the index is the last
        elif index == self.size:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            new_node.prev = current_node
            current_node.next.prev = new_node
            current_node.next = new_node
        self.size += 1

    def __len__(self):
        return self.size

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next

    def __reversed__(self):
        current_node = self.tail
        while current_node is not None:
            yield current_node.value
            current_node = current_node.prev

    def __str__(self):
        values = [str(x) for x in self]
        return " <-> ".join(values)

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, index):
        if index >= self.size:
            raise IndexError("Index out of range")
        return self.get(index)

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
        self.remove(current_node.value)
