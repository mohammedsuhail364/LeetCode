class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum={0:1} # default for empty array 
        cur_sum=0
        res=0
        for n in nums:
            cur_sum+=n
            target=cur_sum-k
            if target in pre_sum:
                res+=pre_sum[target]
            pre_sum[cur_sum]=pre_sum.get(cur_sum,0)+1
        return res