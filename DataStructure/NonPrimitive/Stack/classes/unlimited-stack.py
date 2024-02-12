class Stack:
    class StackEmpty(Exception):
        def __init__(self) -> None:
            super().__init__("Stack is empty")

    def __init__(self):
        self.items = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty:
            raise self.StackEmpty
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty:
            raise self.StackEmpty
        else:
            return self.items[-1]

    def is_empty(self):
        return self.items == []

    def is_full(self):
        return False

    def clear(self):
        self.items = None

    def __str__(self) -> str:
        reversed_items = self.items.reverse()
        str_items = map(str, reversed_items)
        return "\n".join(str_items)
