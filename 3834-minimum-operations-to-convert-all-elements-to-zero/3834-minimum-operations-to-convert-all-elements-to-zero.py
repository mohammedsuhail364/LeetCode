class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # [3,4,3,0,1,2,1,2,5]
        stack=[]
        res=0
        for n in nums:
            while stack and stack[-1]>n:
                stack.pop()
            if n==0:
                continue
            if not stack or stack[-1]<n:
                res+=1
                stack.append(n)
        return res