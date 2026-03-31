class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0
    def push(self, val: int) -> None:
        # index = len(self.stack) - 1
        self.stack.append(val)
        self.size += 1
        

    def pop(self) -> None:
        index = len(self.stack) - 1
        if index >= 0:
            del self.stack[index]
        
    def top(self) -> int:
        index = len(self.stack) - 1
        return self.stack[index]
    
        

    def getMin(self) -> int:
        return min(self.stack)
        
