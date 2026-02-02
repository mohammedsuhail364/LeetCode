class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre_sum={0:1}
        cur_sum=0
        res=0
        for n in nums:
            cur_sum+=n
            target=cur_sum-goal
            if target in pre_sum:
                res+=pre_sum[target]
            if cur_sum not in pre_sum:
                pre_sum[cur_sum]=0
            pre_sum[cur_sum]+=1
        return res


        