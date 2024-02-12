class Node:
    def __init__(self, value, next) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        output = str(self.value)
        while self.next:
            output += " -> " + str(self.next.value)
            self = self.next
        return output

class StackWithMin:
    
    class StackEmptyError(Exception):
        def __init__(self) -> None:
            super().__init__("Stack is empty")
    
    def __init__(self) -> None:
        self.top = None
        self.min_node = None
        
    def min(self):
        if not self.min_node:
            return None
        return self.min_node.value
    
    def push(self, value):
        if self.min_node and (self.min_node.value < value):
            self.min_node = Node(self.min_node.value, self.min_node)
        else:
            self.min_node = Node(value, self.min_node)
        self.top = Node(value, self.top)
    
    def pop(self):
        if not self.top:
            raise self.StackEmptyError
        self.min_node = self.min_node.next
        value = self.top.value
        self.top = self.top.next
        return value
