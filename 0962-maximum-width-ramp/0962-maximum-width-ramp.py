class Solution:
    def maxWidthRamp(self, nums) -> int:
        res=0
        n=len(nums)
        stack=[]
        for i in range(n):
            if not stack or nums[stack[-1]]>nums[i]:
                stack.append(i)
        for j in range(n-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[j]:
                i=stack.pop()
                res=max(res,j-i)
        return res