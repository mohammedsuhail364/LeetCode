class Solution:
    def checkPerfectNumber(self, n: int) -> bool:
        divisors=-n
        for i in range(1,int(sqrt(n))+1):
            if n%i==0:
                if n//i==i:
                   divisors+=i
                else:
                    divisors+=i
                    divisors+=(n//i)
        return divisors==n
                 