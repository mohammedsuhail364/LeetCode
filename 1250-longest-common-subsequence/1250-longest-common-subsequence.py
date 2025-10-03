class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        memo={}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[i,j]
            if i>=n or j>=m:
                return 0
            res=0
            if text1[i]==text2[j]:
                res=1+dfs(i+1,j+1)
            else:
                res=max(dfs(i+1,j),dfs(i,j+1))
            memo[i,j]=res
            return res
        return dfs(0,0)