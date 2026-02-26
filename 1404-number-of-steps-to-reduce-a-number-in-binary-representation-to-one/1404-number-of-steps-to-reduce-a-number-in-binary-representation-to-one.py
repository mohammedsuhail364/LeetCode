class Solution:
    def numSteps(self, s: str) -> int:
        num=int(s,2)
        res=0
        while num!=1:
            if num%2:
                num+=1
            else:
                num=num//2
            res+=1
        return res