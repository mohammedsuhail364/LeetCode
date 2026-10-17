class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache = {} # key -> (val,stamp)
        self.q = deque() # (key,stamp)
        self.time=0
    def _touch(self,key,val):
        self.time+=1
        self.cache [key] = (val,self.time)
        self.q.append((key,self.time))
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value = self.cache[key][0]
        self._touch(key,value)
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache)==self.capacity:
            self._evict()
        self._touch(key,value)

    def _evict(self):
        while self.q:
            k,t = self.q.popleft()
            if k in self.cache and self.cache[k][1]==t:
                del self.cache[k]
                return
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)