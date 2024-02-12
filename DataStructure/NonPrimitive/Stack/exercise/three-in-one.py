class MultiStack:
    
    class StackFullError(Exception):
        def __init__(self) -> None:
            super().__init__("Stack is full")
        
    class StackEmptyError(Exception):
        def __init__(self) -> None:
            super().__init__("Stack is empty")
    
    def __init__(self, stack_size=3) -> None:
        self.num_stacks = 3
        self.stack_size = stack_size
        self.items = [None] * (self.stack_size * self.num_stacks)
        self.sizes = [0] * self.num_stacks
        
        
    def push(self, stack_num, value):
        if self.is_full(stack_num):
            raise self.StackFullError

        index = self.to_index(stack_num)
        self.sizes[index] += 1
        self.items[self.index_of_top(stack_num)] = value
    
    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise self.StackEmptyError
        
        top_index = self.index_of_top(stack_num)
        value = self.items[top_index]
        self.items[top_index] = None
        self.sizes[stack_num] -= 1
        return value
    
    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise self.StackEmptyError
        
        return self.items[self.index_of_top(stack_num)]
    
    def index_of_top(self, stack_num):
        index = self.to_index(stack_num)
        offset = index * self.stack_size
        size = self.sizes[index]
        return offset + size - 1
    
    def is_full(self, stack_num):
        index = self.to_index(stack_num)
        return self.sizes[index] == self.stack_size
    
    def is_empty(self, stack_num):
        index = self.to_index(stack_num)
        return self.sizes[index] == 0

    def to_index(self, stack_num):
        return stack_num - 1
    
    def __str__(self) -> str:
        str_items = map(str, self.items)
        return " ".join(str_items)

    
        

multiple_stack = MultiStack(stack_size=3)
multiple_stack.push(1, 1)
multiple_stack.push(2, 2)
multiple_stack.push(3, 3)
print(multiple_stack)
