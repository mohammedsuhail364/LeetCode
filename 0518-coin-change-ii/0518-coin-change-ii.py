class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for cur in range(amount,-1,-1):
                if cur==amount:
                    dp[i][cur]=1
                    continue
                skip=dp[i+1][cur]
                include=dp[i][cur+coins[i] if cur+coins[i]<=amount else 0]
                dp[i][cur]=skip + include
        return dp[0][0]
        