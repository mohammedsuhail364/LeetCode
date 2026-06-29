class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        # this question just to try every element map with the nums[i] just with bit mask 
        memo={}
        n=len(nums1)
        def dfs(mask):
            if mask==(1<<n )- 1: # all one's eg (111111)
                return 0 # find out all the j's
            if mask in memo:
                return memo[mask]
            i=bin(mask).count('1') # just to find what is the index of i 
            res=inf # we find the minimum so make it max
            for j in range(n):
                if not(mask>>j & 1): # just to check if the j is used or not used in this traversal
                    new_mask = mask | 1<<j 
                    res=min(res,(nums1[i]^nums2[j])+dfs(new_mask))
            memo[mask]=res
            return res
        return dfs(0)