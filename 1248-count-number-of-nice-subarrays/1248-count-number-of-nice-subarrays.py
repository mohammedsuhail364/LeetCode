class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def findSubarrayLessThanOrEqualToK(k):
            res=0
            l=0
            odd=0
            for r in range(len(nums)):
                odd+=(nums[r]%2)
                while l<=r and odd>k:
                    odd-=(nums[l]%2)
                    l+=1
                res+=(r-l+1)
            return res
        return findSubarrayLessThanOrEqualToK(k)-findSubarrayLessThanOrEqualToK(k-1)