class Solution:
    def minElement(self, nums: List[int]) -> int:
        res=float('inf')
        for i in nums:
            k=list(str(i))
            k1=sum(list(map(int,k)))
            if k1<res:
                res=k1
        return res
