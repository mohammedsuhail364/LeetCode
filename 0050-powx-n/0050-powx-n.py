class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if x==0:return 0
            if n==0:return 1
            half=helper(x,n//2)
            if n%2:
                return half*half*x
            return half*half
        res=helper(x,abs(n))
        if n<0:
            return 1/res
        return res