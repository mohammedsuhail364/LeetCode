class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS=len(text1)
        COLS=len(text2)
        dp=[[0]*(COLS+1) for _ in range(ROWS+1)]
        for r in range(ROWS-1,-1,-1):
            for c in range(COLS-1,-1,-1):
                if text1[r]==text2[c]:
                    dp[r][c]=1+dp[r+1][c+1]
                else:
                    dp[r][c]=max(dp[r+1][c],dp[r][c+1])
        return dp[0][0]
