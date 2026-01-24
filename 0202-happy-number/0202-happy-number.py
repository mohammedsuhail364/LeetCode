class Solution:
    def isHappy(self, n: int) -> bool:
        def findNextNumber(n):
            t=0
            while n:
                rem=n%10
                t+=(rem**2)
                n=n//10
            return t
        slow=findNextNumber(n)
        fast=findNextNumber(findNextNumber(n))
        while slow != fast:
            if fast==1: return True
            slow=findNextNumber(slow)
            fast=findNextNumber(findNextNumber(fast))
        return slow==1
            
