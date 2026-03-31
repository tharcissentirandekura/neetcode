class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.size = 0
    def push(self, val: int) -> None:
        # add to both
        self.stack.append(val)
        self.size += 1
    
        # check last value 
        if not self.min_stack or self.min_stack[-1] >= val:
            # val is min here
            self.min_stack.append(val)
        
        

    def pop(self) -> None:
        last = self.stack.pop()
        if last == self.min_stack[-1]:
            self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
    
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
