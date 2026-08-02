class MinStack:

    
    def __init__(self):
        self.min = None
        # self.prevmin = None
        self.stack = []
        self.vals = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.vals) == 0:
            self.vals.append(val)
        elif val < self.vals[-1]:
            self.vals.append(val)
        else:
            self.vals.append(self.vals[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.vals.pop()
            

    def top(self) -> int:
        top = self.stack.pop()
        self.stack.append(top)
        return top

    def getMin(self) -> int:
        return self.vals[-1]
