class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sub_sums={0:1} # empty subarray equals 0 this is for one edge case like if we reach the k at without subtract previous so we handle that 
        cur_sum=0
        res=0
        for n in nums:
            cur_sum+=n
            target=cur_sum-k # if cur_sum-k in the pre_sub_sum means if we subtract that subarray we can get the K
            if target in pre_sub_sums:
                res+=pre_sub_sums[target]
            if cur_sum not in pre_sub_sums:
                pre_sub_sums[cur_sum]=0
            pre_sub_sums[cur_sum]+=1 # add this cur_sum for the future purpose
        return res