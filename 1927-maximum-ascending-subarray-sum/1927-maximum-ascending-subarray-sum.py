class Solution:
    def maxAscendingSum(self, nums) -> int:
        res=0
        i=0
        j=1
        while i<len(nums) and j<len(nums)+1:
            k=nums[i:j]
            flag=True
            for x in range(1,len(k)):
                if k[x-1]>=k[x]:
                    i=j-1
                    j=i+1
                    flag=False
                    break
            if flag:
                res=max(res,sum(k))
            j+=1
        return res