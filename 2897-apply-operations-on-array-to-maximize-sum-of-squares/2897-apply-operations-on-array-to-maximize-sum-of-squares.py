class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        n=len(nums)
        cnt = [0]*31 # tells as a 31 bits
        for x in nums:
            for b in range(31):
                if (x>>b)&1: # check if this bit as a 1 or 0
                    cnt[b]+=1
        val=[]
        for i in range(n):
            v=0
            for b in range(31):
                if cnt[b]>i: # this tells when we use the bits like if we have cnt[2]=1 and i = 2 means already we utilize that 
                    v|=(1<<b)
            val.append(v)
        val.sort(reverse=True)
        return sum(v*v for v in val[:k])%MOD