class MinStack:

    def __init__(self):
        self.stack=[]
        
    def push(self, val: int) -> None:
        min_val=self.getMin()
        if min_val==None or min_val>val:
            min_val=val
        self.stack.append((val,min_val))
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()


    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()