class Router:

    def __init__(self, memoryLimit: int):
        self.n=memoryLimit
        self.q=deque()
        self.visit=set()
        self.dest_to_timestamp=defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source,destination,timestamp) in self.visit:
            return False
        if len(self.q)==self.n:
            old=self.q.popleft()
            self.visit.remove(old)
            _,old_dist,old_time=old
            idx=bisect_left(self.dest_to_timestamp[old_dist],old_time)
            if idx<len(self.dest_to_timestamp[old_dist]) and self.dest_to_timestamp[old_dist][idx]==old_time:
                self.dest_to_timestamp[old_dist].pop(idx)
        self.q.append((source,destination,timestamp))
        self.visit.add((source,destination,timestamp))
        bisect.insort(self.dest_to_timestamp[destination],timestamp)
        return True    

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        packet=self.q.popleft()
        self.visit.remove(packet)
        _,dist,time=packet
        idx=bisect_left(self.dest_to_timestamp[dist],time)
        if idx<len(self.dest_to_timestamp[dist]) and self.dest_to_timestamp[dist][idx]==time:
            self.dest_to_timestamp[dist].pop(idx)
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        arr=self.dest_to_timestamp[destination]
        left=bisect_left(arr,startTime)
        right=bisect_right(arr,endTime)
        return right-left # dont include the right thats why we dont add +1

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)