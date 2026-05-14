class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
        n=len(nums)
        if n==1:
            return False
        c=Counter(nums)
        for i in range(1,len(nums)):
            if i not in c:
                return False
            if i==n-1 and c[i]!=2:
                return False
        return True