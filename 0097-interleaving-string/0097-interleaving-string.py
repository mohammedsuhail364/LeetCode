class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False 
        n=len(s1)
        m=len(s2)
        dp=[[False]*(m+1) for _ in range(n+1)] 
        dp[n][m]=True # base case if we reach this we can use all the strings 
        for i in range(n,-1,-1):
            for j in range(m,-1,-1):
                k=i+j
                if i==m and j==n:
                    continue # already set this
                
                if i<len(s1) and s1[i]==s3[k]:
                    dp[i][j] =dp[i][j] or dp[i+1][j]
                if not dp[i][j] and j<len(s2) and s2[j]==s3[k]:
                    dp[i][j] =dp[i][j] or dp[i][j+1]
        return dp[0][0]