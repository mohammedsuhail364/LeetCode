# https://www.youtube.com/watch?v=U0o7SJqZonI&t=4s
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod=10**9+7
        groups=[]
        count=1
        for i in range(len(word)-1):
            if word[i]==word[i+1]:
                count+=1
            else:
                groups.append(count)
                count=1
        groups.append(count)
        total_ways=1
        for i in groups:
            total_ways=(total_ways*i)%mod
        if len(groups)>=k:
            return total_ways
        prefix_sum=[1]*k
        for g in groups:
            dp=[0]*k
            for length in range(1,k):
                dp[length]=prefix_sum[length-1] 
                if length-g-1>=0: # negative checking
                    dp[length]=(dp[length]-prefix_sum[length-g-1])%mod
            prefix_sum=[0]*k
            prefix_sum[0]=dp[0]
            for i in range(1,k):
                prefix_sum[i]=(prefix_sum[i-1]+dp[i])%mod
        return (total_ways-prefix_sum[k-1])%mod
        