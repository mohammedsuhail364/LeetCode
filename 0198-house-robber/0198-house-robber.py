class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}
        def backtrack(i,amo):
            if i>=len(nums):
                return amo
            if (i,amo) in dp:
                return dp[(i,amo)]
            # skip the current one
            skip=backtrack(i+1,amo)
            # add the current one
            include=backtrack(i+2,amo+nums[i])
            dp[(i,amo)]=max(skip,include)
            return dp[(i,amo)]
        return backtrack(0,0)
        