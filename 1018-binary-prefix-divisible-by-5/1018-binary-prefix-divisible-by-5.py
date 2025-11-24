class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        prefix=""
        res=[]
        for n in nums:
            prefix+=str(n)    
            res.append((int(prefix,2))%5==0)
        return res