import heapq

class Solution:
    def closestPrimes(self, left: int, right: int):
        def get_prime():
            is_prime=[True]*(right+1)
            is_prime[0]=is_prime[1]=False
            for n in range(2,int(right**0.5)+1):
                if not is_prime[n]:
                    continue
                for m in range(n+n,right+1,n):
                    is_prime[m]=False
            prime=[]
            for x in range(len(is_prime)):
                if is_prime[x] and x>=left:
                    prime.append(x)
            return prime

        prime=get_prime()
        res=[-1,-1]
        diff=(right+1)
        for x in range(1,len(prime)):
            val=prime[x]-prime[x-1]
            if val<diff:
                diff=val
                res[0],res[1]=prime[x-1],prime[x]
        return res