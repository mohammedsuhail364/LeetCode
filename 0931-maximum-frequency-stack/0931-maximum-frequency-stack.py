class FreqStack:

    def __init__(self):
        self.max_cnt=0
        self.stacks={}
        self.freq={}

    def push(self, val: int) -> None:
        val_cnt=1+self.freq.get(val,0)
        self.freq[val]=val_cnt
        if val_cnt>self.max_cnt:
            self.max_cnt=val_cnt
            self.stacks[val_cnt]=[]
        self.stacks[val_cnt].append(val)

    def pop(self) -> int:
        res=self.stacks[self.max_cnt].pop()
        self.freq[res]-=1
        if not self.stacks[self.max_cnt]:
            self.max_cnt-=1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()