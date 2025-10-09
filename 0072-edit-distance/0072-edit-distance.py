class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # refer neetcode
        n=len(word1)
        m=len(word2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][m]=n-i
        for j in range(m):
            dp[n][j]=m-j
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    insert=dp[i][j+1]
                    delete=dp[i+1][j]
                    replace=dp[i+1][j+1]
                    dp[i][j]=1+min(insert,delete,replace)
        return dp[0][0]