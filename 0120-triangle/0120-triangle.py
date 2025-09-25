class Solution:
    def minimumTotal(self, triangle) -> int:
        memo={}
        def backtrack(x,i):
            if (x,i) in memo:
                return memo[x,i]
            if x==len(triangle)-1:
                memo[x,i]=triangle[x][i]
                return memo[x,i]
            left=backtrack(x+1,i)
            right=backtrack(x+1,i+1)
            memo[x,i]=triangle[x][i]+min(left,right)
            return memo[x,i]
        return backtrack(0,0)
        