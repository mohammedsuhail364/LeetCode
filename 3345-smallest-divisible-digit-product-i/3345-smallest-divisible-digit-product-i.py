class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def findValue(x):
            res=1
            while x:
                t=x%10
                if t==0:
                    return 0
                res=res*t
                x=x//10
            return res
        for x in range(n,101):
            val=findValue(x)
            if val%t==0 and x>=n:
                return x