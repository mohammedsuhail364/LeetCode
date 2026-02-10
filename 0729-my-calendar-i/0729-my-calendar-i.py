class MyCalendar:

    def __init__(self):
        self.store=[]

    def book(self, startTime: int, endTime: int) -> bool:
        for s,e in self.store:
            if s<=startTime<e or s<=endTime-1<e:
                return False
        self.store.append((startTime,endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)