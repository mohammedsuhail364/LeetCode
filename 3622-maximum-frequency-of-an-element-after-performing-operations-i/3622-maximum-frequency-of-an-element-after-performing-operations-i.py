class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n=max(nums)
        count=[0]*(n+1)
        for i in nums:
            count[i]+=1
        presum=[0]
        for i in range(n+1):
            presum.append(presum[-1]+count[i])
        res=0
        for i in range(n+1):
            left=presum[i]-presum[max(0,i-k)]
            right=presum[min(n+1,i+k+1)]-presum[i+1]
            cur=count[i]+min(numOperations,left+right)
            res=max(res,cur)
        return res

