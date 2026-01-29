class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        pre_sum={0:1}
        cur_sum=0
        res=0
        for n in nums:
            cur_sum+=n
            target=cur_sum%k
            if target in pre_sum:
                res+=pre_sum[target]
            if target not in pre_sum:
                pre_sum[target]=0
            pre_sum[target]+=1
        return res