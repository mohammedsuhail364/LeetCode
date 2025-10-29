class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maximum=max(nums)+k+1
        count=[0]*(maximum)
        for i in nums:
            count[i]+=1

        for i in range(1,maximum):
            count[i]=count[i-1]+count[i]
        res=0
        for i in range(1,maximum):
            left=max(0,i-k)
            right=min(maximum-1,i+k)
            left_most=max(0,left-1)
            total=count[right]-count[left_most]
            freq=count[i]-count[i-1]
            res=max(res,freq+min(total-freq,numOperations))
        return res



        