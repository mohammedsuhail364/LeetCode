class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[0][0]=True # find the correct one
        for j in range(1,len(p)+1):
            dp[0][j]=dp[0][j-1] and p[j-1]=="*"
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1): 
                if s[i-1]==p[j-1] or p[j-1]=="?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=="*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j]=False
        return dp[len(s)][len(p)]
        memo={}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[i,j]
            if i<0 and j<0:
                return True # find the correct one
            if i>=0 and j<0:
                return False # we can have some chars in s, return false
            if i<0 and j>=0:
                # we have some values in p but what if all are "*" we return true right?
                return all(x=="*" for x in p[:j+1])
            # check the match 
            if s[i]==p[j] or p[j]=="?":
                memo[i,j] = dfs(i-1,j-1)
                return memo[i,j]
            if p[j]=="*":
                # check the two case dont use the star or use it for a char
                memo[i,j] = dfs(i,j-1) or dfs(i-1,j)
                return memo[i,j]
            memo[i,j] = False
            return memo[i,j]
        return dfs(len(s)-1,len(p)-1)