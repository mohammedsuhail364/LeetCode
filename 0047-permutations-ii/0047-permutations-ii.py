from typing import List
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        count=Counter(nums)
        def dfs(path):
            if len(path)==len(nums):
                res.append(path)
                return 
            for n in count:
                if count[n]>0:
                    count[n]-=1
                    dfs(path+[n])
                    count[n]+=1
        dfs([])
        return res