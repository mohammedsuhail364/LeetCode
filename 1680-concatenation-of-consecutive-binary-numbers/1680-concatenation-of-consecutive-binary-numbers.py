class Solution:
    def concatenatedBinary(self, n: int) -> int:
        start=''
        for i in range(1,n+1):
            start+=bin(i)[2:]
        k=int(start,2)%(10**9+7)
        return k