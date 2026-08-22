class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def getSumAndProductOfDigits(n):
            s,m=0,1
            while n:
                t=n%10
                s+=t
                m*=t
                n=n//10
            return s+m
        s = getSumAndProductOfDigits(n)
        return (n%s==0) 