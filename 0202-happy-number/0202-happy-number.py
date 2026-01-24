class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while True:
            if n in seen:
                return False
            if n==1:
                return True
            seen.add(n)
            t=0
            while n:
                rem=n%10
                t+=(rem**2)
                n=n//10
            n=t
