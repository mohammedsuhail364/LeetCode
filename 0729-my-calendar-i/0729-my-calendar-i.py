class MyCalendar:

    def __init__(self):
        self.store=[]

    def book(self, startTime: int, endTime: int) -> bool:
        for s,e in self.store:
             if max(startTime,s)<min(endTime,e):
                return False
        self.store.append((startTime,endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)