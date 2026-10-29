class MapSum:

    def __init__(self):
        self.hashmap = {}

    def insert(self, key: str, val: int) -> None:
        self.hashmap[key] = val

    def sum(self, prefix: str) -> int:
        res=0
        for key,val in self.hashmap.items():
            if key.startswith(prefix):
                res+=val
        return res
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)