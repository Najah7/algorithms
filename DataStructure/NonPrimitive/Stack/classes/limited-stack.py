class LimitedStack:
    class StackFullError(Exception):
        def __init__(self) -> None:
            super().__init__("Stack is full")

    class StackEmptyError(Exception):
        def __init__(self) -> None:
            super().__init__("Stack is empty")

    def __init__(self, length=10):
        self.items = [None] * length
        self.length = length

    def push(self, item):
        if self.is_full():
            raise self.StackFullError
        else:
            self.stack.append(item)

    def pop(self):
        if self.is_empty:
            raise self.StackEmptyError
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty:
            raise self.StackEmptyError
        else:
            return self.items[-1]

    def is_empty(self):
        return self.items == []

    def is_full(self):
        return len(self.items) >= self.length

    def clear(self):
        self.items = None

    def __str__(self) -> str:
        reversed_items = self.items.reverse()
        str_items = map(str, reversed_items)
        return "\n".join(str_items)
