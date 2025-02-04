class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                k=nums[i:j]
                flag=True
                for x in range(1,len(k)):
                    if k[x-1]>=k[x]:
                        flag=False
                        break
                if flag:
                    res=max(res,sum(k))
        return res