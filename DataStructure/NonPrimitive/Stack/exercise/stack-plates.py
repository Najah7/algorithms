class PlateStack:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        
    def push(self, value):
        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(value)
    
    def pop(self):
        if len(self.stacks) == 0:
            return None
        value = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return value

    def pop_at(self, stack_num):
        if not (0 <= stack_num < len(self.stacks)):
            return None
        
        value = self.stacks[stack_num].pop()
        if len(self.stacks[stack_num]) == 0:
            self.stacks.pop(stack_num)
        return value
    
    def __str__(self) -> str:
        return self.stacks
