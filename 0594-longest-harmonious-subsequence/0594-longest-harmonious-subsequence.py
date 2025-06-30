class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c=Counter(nums)
        res=0
        for num in nums:
            if num+1 in c:
                tmp=c[num]+c[num+1]
                res=max(tmp,res)
        return res