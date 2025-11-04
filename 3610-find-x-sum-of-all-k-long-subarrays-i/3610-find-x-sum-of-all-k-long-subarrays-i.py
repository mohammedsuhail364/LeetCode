from collections import Counter
from typing import List
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def getTopXvalues(arr):
            freq=sorted(Counter(arr).items(),key=lambda x:(x[1],x[0]),reverse=True)
            res=0
            temp=0
            for i,j in freq:
                if temp==x:
                    break
                res+=(i*j)
                temp+=1
            return res
        i=0 
        j=k
        res=[]
        while j<=len(nums):
            arr=nums[i:j]
            res.append(getTopXvalues(arr))
            i+=1
            j+=1
        return res