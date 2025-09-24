class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_valid(s,e):
            tmp=sorted(nums[s:e+1])
            res=set()
            for i in range(len(tmp)-1):
                res.add(tmp[i]-tmp[i+1])
            return len(res)==1
        res=[]
        for s,e in zip(l,r):
            if is_valid(s,e):
                res.append(True)
            else:
                res.append(False)
        return res