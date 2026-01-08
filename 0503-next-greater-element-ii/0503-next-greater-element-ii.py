class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[-1]*len(nums)
        stack=[] # store only index
        for i in range(len(nums)*2):
            n=nums[i%len(nums)]
            while stack and nums[stack[-1]]<n:
                idx=stack.pop()
                res[idx]=n
            if i<len(nums):
                stack.append(i)
        return res
