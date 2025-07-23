class FreqStack:

    def __init__(self):
        self.freq=defaultdict(int)
        self.count=defaultdict(list)

    def push(self, val: int) -> None:
        self.freq[val]+=1
        self.count[self.freq[val]].append(val)

    def pop(self) -> int:
        max_val=max(self.freq.values())
        if self.count[max_val]:
            self.freq[self.count[max_val][-1]]-=1
            return self.count[max_val].pop()

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()