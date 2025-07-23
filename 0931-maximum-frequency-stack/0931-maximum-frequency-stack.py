class FreqStack:

    def __init__(self):
        self.stack=[]
        self.freq=defaultdict(int)
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val]+=1

    def pop(self) -> int:

        max_val=max(self.freq.values())
        for i in range(len(self.stack)-1,-1,-1):
            if max_val==self.freq[self.stack[i]]:
                self.freq[self.stack[i]]-=1
                return self.stack.pop(i)
                


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()