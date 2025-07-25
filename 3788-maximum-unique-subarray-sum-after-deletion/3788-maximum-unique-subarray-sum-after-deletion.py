class Solution:
    def maxSum(self, nums: List[int]) -> int:
        c=Counter(nums)
        res=0
        res1=-inf
        for i in c:
            if i>0:
                res+=i
        for i in c:
            if i<0:
                res1=max(i,res1)
        if (res in c )or res:
            return res
        return res1