import heapq

class Solution:
    def closestPrimes(self, left: int, right: int):
        def get_prime():
            is_prime=[True]*(right+1)
            is_prime[0]=is_prime[1]=False
            for n in range(2,right+1):
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
        final_res=[-1,-1]
        i=0
        j=1
        diff=float('inf')
        while j<len(prime):
            val=prime[j]-prime[i]
            if val<diff:
                diff=val
                final_res[0]=prime[i]
                final_res[1]=prime[j]
            i+=1
            j+=1
        return final_res