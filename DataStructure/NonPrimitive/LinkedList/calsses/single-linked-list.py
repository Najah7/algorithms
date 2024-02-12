import typing as t


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self, *args):
        self.size = 0
        if args:
            for data in args:
                self.append(data)
                self.size += 1
        else:
            self.head = None
            self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert(self, index, data):
        if not (0 <= index < self.size):
            raise IndexError
        new_node = Node(data)
        if index == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 2):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def find(self, data):
        current = self.head
        index = 0

        # traverse the list
        while current is not None:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def find_middle(self):
        # known size of the list
        mid = self.size // 2
        current = self.head
        for _ in range(mid):
            current = current.next
        return current

        # unknown size of the list
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            slow, fast = slow.next, fast.next.next

        return slow

    def get(self, index):
        if not (0 <= index < self.size):
            raise IndexError

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def pop(self):
        if self.head is None:
            raise Exception("pop from empty list")

        current = self.head
        while current.next is not None:
            previous = current
            current = current.next
        previous.next = None
        self.size -= 1
        return current.data

    def pop_first(self):
        if self.head is None:
            raise Exception("pop from empty list")

        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def traverse(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("index out of range")

        # when selected index is 0 (first node)
        if index == 0:
            popped_node = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            popped_node.next = None
            self.length -= 1
            return popped_node

        else:
            previous = self.head
            for _ in range(index - 1):
                previous = previous.next

            popped_node = previous.next

            # when selected index is the last node
            if popped_node.next is None:
                self.tail = previous

            previous.next = previous.next.next
            popped_node.next = None
            self.length -= 1
            return popped_node

    def remove_duplicates(self):
        if self.head is None:
            return

        node_values = set()
        current = self.head
        node_values.add(current.data)

        while current.next:
            if current.data in node_values:
                previous.next = previous.next.next
                self.size -= 1
            else:
                node_values.add(current.data)
                previous = current
            current = current.next

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    # private methods

    def __len__(self):
        return self.size

    def __iter__(self):
        current: t.Union[Node, None] = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, data):
        if not (0 <= index < self.size):
            raise IndexError
        current: t.Union[Node, None] = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def __delitem__(self, index):
        if not (0 <= index < self.size):
            raise IndexError
        if index == 0:
            self.head = self.head.next
        else:
            current: t.Union[Node, None] = self.head
            for _ in range(index - 2):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def __repr__(self):
        return " -> ".join(str(data) for data in self)

    def __str__(self):
        return " -> ".join(str(data) for data in self)

    def __add__(self, other):
        new_list = SingleLinkedList()
        for data in self:
            new_list.append(data)
        for data in other:
            new_list.append(data)
        return new_list

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for data1, data2 in zip(self, other):
            if data1 != data2:
                return False
        return True

    def __ne__(self, other):
        return not self == other

    def __contains__(self, data):
        for current in self:
            if current == data:
                return True
        return False

    def __reversed__(self):
        prev_node = None
        current_node = self.head

        # change the direction of links
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        # switch head and tail
        self.head, self.tail = self.tail, self.head
        return self
