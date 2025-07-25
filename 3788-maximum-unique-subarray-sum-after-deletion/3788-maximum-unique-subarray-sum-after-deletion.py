class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        c=Counter(nums)
        res=0
        for i in c:
            if i>0:
                res+=i
        return res