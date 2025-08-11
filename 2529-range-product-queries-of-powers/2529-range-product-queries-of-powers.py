from typing import List
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod=10**9+7
        bin_n=bin(n)[2:]
        powers=[]
        j=0
        for i in reversed(range(len(bin_n))):
            if bin_n[i]=='1':
                powers.append(2**j)
            j+=1
        res=[]
        for l,r in queries:
            prod=1
            for x in range(l,r+1):
                prod=(prod*powers[x])%mod
            res.append(prod)
        return res