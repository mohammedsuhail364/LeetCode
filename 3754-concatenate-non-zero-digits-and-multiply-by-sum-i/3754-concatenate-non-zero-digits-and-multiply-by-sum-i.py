class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        def sum_numbers(n):
            n=int(n)
            res=0
            while n:
                res+=(n%10)
                n=n//10
            return res
        k=str(n).replace("0","")
        s=sum_numbers(k)
        return int(k)*s