class MyStack:

    def __init__(self):
        self.li=[]

    def push(self, x: int) -> None:
        self.li.append(x)

    def pop(self) -> int:
        k=self.li.pop()
        return k 
    def top(self) -> int:
        return self.li[-1]

    def empty(self) -> bool:
        if self.li==[]:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()