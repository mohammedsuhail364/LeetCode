class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod=(10**9)+7
        res=0
        dp=[0]*(n+1)
        dp[1]=1
        for i in range(1,n+1):
            for j in range(i+delay,min(n,i+forget-1)+1):
                dp[j]=(dp[j]+dp[i])%mod
        for i in range(1,n+1):
            if i+forget>n: # the person didnt forget the secret
                res=(res+dp[i])%mod
        return res