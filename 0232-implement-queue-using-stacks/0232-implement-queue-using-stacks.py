class MyQueue:

    def __init__(self):
        self.li=[]

    def push(self, x: int) -> None:
        self.li.append(x)


    def pop(self) -> int:
        return self.li.pop(0)

    def peek(self) -> int:
        return self.li[0]

    def empty(self) -> bool:
        if self.li==[]:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()