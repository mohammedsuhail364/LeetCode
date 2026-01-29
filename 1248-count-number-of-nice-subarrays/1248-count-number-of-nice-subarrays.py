class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        def count_subarray_less_than_k(k):
            l=0
            odd=0
            res=0
            for r in range(len(nums)):
                odd+=nums[r]%2
                while odd>k:
                    odd-=nums[l]%2
                    l+=1
                res+=(r-l)
            return res
        return count_subarray_less_than_k(k)-count_subarray_less_than_k(k-1)
