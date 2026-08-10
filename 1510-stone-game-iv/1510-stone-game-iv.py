class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp=[False]*(n+1)
        for i in range(1,n+1):
            sq=1
            while sq*sq <=i:
                if not dp[i-sq*sq]:
                    dp[i]=True
                    break
                sq+=1
        return dp[n]
