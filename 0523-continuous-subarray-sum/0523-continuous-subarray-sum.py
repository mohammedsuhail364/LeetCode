from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_sum={0:-1}
        cur_sum=0
        for r in range(len(nums)):
            cur_sum+=nums[r]
            target=cur_sum%k
            if target in pre_sum and r - pre_sum[target] > 1:
                return True
            if target not in pre_sum:
                pre_sum[target]=r
        return False
