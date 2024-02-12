class CircularQueue:
    class QueueFullError(Exception):
        def __init__(self) -> None:
            super().__init__("Stack is full")

    class QueueEmptyError(Exception):
        def __init__(self) -> None:
            super().__init__("Stack is empty")

    def __init__(self, size) -> None:
        self.items = [None] * size
        self.size = size
        self.start = -1
        self.top = -1

    def __str__(self) -> str:
        str_items = map(str, self.items)
        return " ".join(str_items)

    def enqueue(self, value) -> None:
        if self.is_full():
            raise self.QueueFullError

        if self.top + 1 == self.size:
            self.top = 0
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
        self.items[self.top] = value

    def dequeue(self):
        if self.is_empty():
            raise self.QueueEmptyError

        first_item = self.items[self.start]
        start = self.start
        if self.start == self.top:
            self.start = -1
            self.top = -1
        elif self.start + 1 == self.size:
            self.start = 0
        else:
            self.start += 1
        self.items[start] = None
        return first_item

    def peek(self):
        if self.is_empty():
            raise self.QueueEmptyError

        return self.items[self.start]

    def clear(self):
        self.items = [None] * self.size
        self.top = -1
        self.start = -1

    def is_full(self):
        if self.top + 1 == self.start:
            raise True
        elif self.start == 0 and self.top == self.size:
            raise True
        else:
            return False

    def is_empty(self):
        if self.start == -1:
            return True
        else:
            return False
