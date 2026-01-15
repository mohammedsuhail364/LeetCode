class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # refer this question 907. Sum of Subarray Minimums
        # because we already find the subarray minimums now we only find the subarray maximums 
        # subarray maximum - sub array minimum
        n=len(nums)
        stack=[]
        def findNSE():
            nse=[n]*n
            stack.clear() # for reuse the stack
            for i in range(n):
                while stack and nums[stack[-1]]>nums[i]:
                    idx=stack.pop()
                    nse[idx]=i
                stack.append(i)
            return nse
        def findNGE():
            nge=[n]*n
            stack.clear() # for reuse the stack
            for i in range(n):
                while stack and nums[stack[-1]]<nums[i]:
                    idx=stack.pop()
                    nge[idx]=i
                stack.append(i)
            return nge
        def findPSEE():
            pse=[-1]*n
            stack.clear()
            for i in range(n):
                while stack and nums[stack[-1]]>nums[i]:
                    stack.pop()
                if stack:
                    pse[i]=stack[-1]
                stack.append(i)
            return pse
        def findPGEE():
            pge=[-1]*n
            stack.clear()
            for i in range(n):
                while stack and nums[stack[-1]]<nums[i]:
                    stack.pop()
                if stack:
                    pge[i]=stack[-1]
                stack.append(i)
            return pge
        nse=findNSE()
        nge=findNGE()
        pse=findPSEE()
        pge=findPGEE()
        # subarray minimum
        min_val=0
        for i in range(n):
            left=i-pse[i]
            right=nse[i]-i
            min_val+=(nums[i]*left*right)
        # subarray maximum
        max_val=0
        for i in range(n):
            left=i-pge[i]
            right=nge[i]-i
            max_val+=(nums[i]*left*right)
        return max_val-min_val
        