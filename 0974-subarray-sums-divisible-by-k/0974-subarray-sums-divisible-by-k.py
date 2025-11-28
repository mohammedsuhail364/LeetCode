from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        pre_sum=0
        
        seen=defaultdict(int)
        seen[0]=1 # refers if the eg like this nums=[5] and k=5 we can iterate this temp=5%5=0 then we can search in seen but it gives zero if we dont initialize 
        res=0
        for n in nums:
            pre_sum+=n
            temp=pre_sum%k
            res+=seen[temp]
            seen[temp]+=1
        return res