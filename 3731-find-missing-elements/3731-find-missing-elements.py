class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        seen=set(nums)
        s=min(nums)
        e=max(nums)
        res=[]
        for x in range(s,e+1):
            if x not in seen:
                res.append(x)
        return res