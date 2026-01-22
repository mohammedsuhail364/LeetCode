class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum={0:1} # empty subarray has 0
        res=0
        prefix_i=0
        for n in nums:
            prefix_i+=n # this indicates the current sum prefix[i]
            prefix_j=prefix_i-k # this indicates prefix[i] - prefix[j] = k if we subtract the prefix of j we get the k value
            if prefix_j in prefix_sum:
                res+=prefix_sum[prefix_j]
            if prefix_i not in prefix_sum:
                prefix_sum[prefix_i]=0
            prefix_sum[prefix_i]+=1
        return res
            
            