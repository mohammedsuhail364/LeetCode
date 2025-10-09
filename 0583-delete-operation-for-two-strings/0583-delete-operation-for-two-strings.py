class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # similiar to edit distance and LCS question
        n,m=len(word1),len(word2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][m]=(n-i)
        for j in range(m):
            dp[n][j]=(m-j)
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    delete_from_word1=dp[i+1][j]
                    delete_from_word2=dp[i][j+1]
                    dp[i][j]=1+min(delete_from_word1,delete_from_word2)
        return dp[0][0]