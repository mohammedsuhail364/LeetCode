class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]: 
        res=[]
        cur=0
        for n in nums:
            cur=(cur<<1 | n)
            res.append(cur%5==0)
        return res