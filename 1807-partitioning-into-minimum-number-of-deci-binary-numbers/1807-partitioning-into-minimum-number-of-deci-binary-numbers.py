class Solution:
    def minPartitions(self, n: str) -> int:
        s=set(n)
        for i in range(9,0,-1):
            if str(i) in s:
                return i