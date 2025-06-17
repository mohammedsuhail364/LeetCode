class Solution:
    def myPow(self, a: float, b: int) -> float:
        res=1
        power=abs(b)
        while power>0:
            if power%2:
                res*=a
            a=a*a
            power=power//2
        return res if b>=0 else 1/res