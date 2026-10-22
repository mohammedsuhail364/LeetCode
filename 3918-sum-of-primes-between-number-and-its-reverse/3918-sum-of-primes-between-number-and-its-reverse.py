class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        def is_prime(x):
            if x<=1:return False
            for i in range(2,int(x**0.5)+1):
                if x%i==0:return False
            return True
        rev = int(str(n)[::-1])
        low,high = min(rev,n),max(rev,n)
        res=0
        for x in range(low,high+1):
            if is_prime(x):
                res+=x
        return res