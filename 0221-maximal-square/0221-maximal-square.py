class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # refer neetcode
        ROWS,COLS=len(matrix),len(matrix[0])
        memo={}
        def dfs(r,c):
            if r>=ROWS or c>=COLS:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            memo[(r,c)]=0   
            down=dfs(r+1,c)
            right=dfs(r,c+1)
            diagonal=dfs(r+1,c+1)
            if matrix[r][c]=="1":
                memo[(r,c)]=1+min(down,right,diagonal)
            return memo[(r,c)]
        dfs(0,0)
        return max(memo.values())**2