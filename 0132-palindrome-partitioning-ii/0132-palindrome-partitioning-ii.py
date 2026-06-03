class Solution:
    def minCut(self, s: str) -> int:
        # this question basically find the minimum cuts
        # what i m doing in this question is find the minimum partiton of the palindrome word and -1 to the res because we need cuts
        # when convert from the memo -> Tabulation follow these steps
        n=len(s)
        # identify the states dfs(i)->dp[i]
        dp=[0]*(n+1)
        # identify the base case if i>=len(s): return 0
        # already we set as 0
        # precompute the palindrome
        is_palindrome=[[False]*(n) for _ in range(n)]
        for i in range(n-1,-1,-1): # once again want to revisit this palindrome portion
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or is_palindrome[i+1][j-1]):
                    is_palindrome[i][j]=True
        # iterate from right to left
        for i in range(n-1,-1,-1):
            temp=""
            res=inf
            for j in range(i,n):
                temp+=s[j]
                if is_palindrome[i][j]:
                    cost=1+dp[j+1]
                    res=min(res,cost)
                dp[i]=res
        return dp[0]-1
