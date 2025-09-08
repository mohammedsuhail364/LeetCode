class MyCalendarTwo:

    def __init__(self):
        self.bookings=[]
        self.overlap=[]
    def book(self, startTime: int, endTime: int) -> bool:
        for start,end in self.overlap:
            if not (startTime>=end or endTime<=start):
                return False
        for start,end in self.bookings:
            if not (startTime>=end or endTime<=start):
                self.overlap.append([max(start,startTime),min(end,endTime)])
        self.bookings.append([startTime,endTime])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)