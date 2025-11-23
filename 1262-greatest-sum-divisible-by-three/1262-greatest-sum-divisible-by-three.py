class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total=sum(nums)
        if total%3==0:
            return total
        # when we mod the total it is either 1 or 2 or 0 we can handle the 0
        mod1=[]
        mod2=[]
        for n in nums:
            if n%3==1:
                mod1.append(n)
            elif n%3==2:
                mod2.append(n)
        mod1.sort()
        mod2.sort()
        if total%3==1:
            option1=mod1[0] if len(mod1)>=1 else inf
            option2=sum(mod2[:2]) if len(mod2)>=2 else inf
            return total-min(option1,option2)
        else: # total%3==2
            option1=mod2[0] if len(mod2)>=1 else inf
            option2=sum(mod1[:2]) if len(mod1)>=2 else inf
            return total-min(option1,option2)
