class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # refer neetcode
        dp=[[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        print(dp)
        for r in range(len(text1)-1,-1,-1):
            for c in range(len(text2)-1,-1,-1):
                if text1[r]==text2[c]:
                    dp[r][c]=1+dp[r+1][c+1]
                else:
                    dp[r][c]=max(dp[r+1][c],dp[r][c+1])
        return dp[0][0]
    
                