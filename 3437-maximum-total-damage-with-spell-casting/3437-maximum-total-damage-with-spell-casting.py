class Solution:
    def maximumTotalDamage(self, power) -> int:

        count=Counter(power)
        unique=sorted(count.keys())
        dp=[0]*(len(unique)+1)
        for i in range(len(unique)-1,-1,-1):
            val=unique[i]
            j=bisect.bisect_right(unique,val+2)
            take=val*count[val]+dp[j]
            skip=dp[i+1]
            dp[i]=max(skip,take)
        return dp[0]
       