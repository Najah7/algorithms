class Queue:
    class QueueEmptyError(Exception):
        def __init__(self) -> None:
            super().__init__("Stack is Empty")

    def __init__(self) -> None:
        self.items = []
        self.length = 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise self.QueueEmptyError
        else:
            return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise self.QueueEmptyError
        else:
            return self.items[0]

    def is_empty(self):
        return self.items == []

    def clear(self):
        self.items = None

    def __str__(self) -> str:
        items = [str(item) for item in self.items]
        return " ".join(items)
