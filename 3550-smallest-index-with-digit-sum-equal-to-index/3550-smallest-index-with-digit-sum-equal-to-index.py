class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def findSum(n):
            res=0
            while n:
                res+=n%10
                n//=10
            return res
        for i in range(len(nums)):
            x=findSum(nums[i])
            if x==i:
                return i
        return -1