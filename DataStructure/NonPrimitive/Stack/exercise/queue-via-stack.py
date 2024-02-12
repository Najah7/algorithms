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
    
    def is_empty(self):
        return self.items == []
    
    def __str__(self) -> str:
        reversed_items = self.items.reverse()
        str_items = map(str, reversed_items)
        return "\n".join(str_items)
    
    def __len__(self):
        return len(self.items)

class QueueViaStack:
    
    def __init__(self):
        self.input_stack = Stack()
        self.output_stack = Stack()
    
    def enqueue(self, item):
        self.input_stack.push(item)
    
    def dequeue(self):
        if self.output_stack.is_empty():
            while not self.input_stack.is_empty():
                self.output_stack.push(self.input_stack.pop())
        dequeued_value =  self.output_stack.pop()
        while not self.output_stack.is_empty():
            self.input_stack.push(self.output_stack.pop())
        return dequeued_value
