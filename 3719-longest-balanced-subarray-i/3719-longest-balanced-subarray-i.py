class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            even=set()
            odd=set()
            for j in range(i,len(nums)):
                if nums[j]%2:
                    odd.add(nums[j])
                else:
                    even.add(nums[j])
                if len(odd)==len(even):
                    res=max(res,j-i+1)
        return res