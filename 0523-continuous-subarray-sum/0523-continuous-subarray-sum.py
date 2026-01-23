class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        cur_sum=0
        seen={0:-1}
        for r in range(len(nums)):
            cur_sum+=nums[r]
            cur_sum=cur_sum%k
            if cur_sum in seen:
                if r - seen[cur_sum]>=2:
                    return True
            else:
                seen[cur_sum]=r
        return False


