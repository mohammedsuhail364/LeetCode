from typing import List
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        bin_n=bin(n)[2:]
        powers=[]
        mod=10**9+7
        j=0
        for i in reversed(range(len(bin_n))):
            if bin_n[i]=='1':
                powers.append(2**j)
            j+=1
        pre_sum=powers[:]
        
        for i in range(1,len(pre_sum)):
            pre_sum[i]=pre_sum[i-1]*pre_sum[i]
        res=[]
        for l,r in queries:
            val=pre_sum[l-1] if l-1>=0 else 1
            res.append((pre_sum[r]//val)%mod)
        return res