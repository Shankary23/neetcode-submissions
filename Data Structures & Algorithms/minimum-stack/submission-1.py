class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.MinStack:
            self.MinStack.append(min(self.MinStack[-1],val))
        else:
            self.MinStack.append(val)
    
        

    def pop(self) -> None:
        self.stack.pop()
        # print(removed)
        self.MinStack.pop()
        # print(self.stack)
        # print(self.MinStack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
