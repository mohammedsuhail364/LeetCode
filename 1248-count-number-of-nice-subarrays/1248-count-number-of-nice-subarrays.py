class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        pre_sum={0:1}
        odd=0
        res=0
        for i in nums:
            if i%2:
                odd+=1
            target=odd-k
            if target in pre_sum:
                res+=pre_sum[target]
            if odd not in pre_sum:
                pre_sum[odd]=0
            pre_sum[odd]+=1
        return res
