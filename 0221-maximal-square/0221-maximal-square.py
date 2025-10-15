class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # refer neetcode
        ROWS,COLS=len(matrix),len(matrix[0])
        dp=[[0]*(COLS+1) for _ in range(ROWS+1)]
        for r in range(ROWS-1,-1,-1):
            for c in range(COLS-1,-1,-1):
                down=dp[r+1][c]
                right=dp[r][c+1]
                diagonal=dp[r+1][c+1]
                if matrix[r][c]=="1":
                    dp[r][c]=1+min(down,right,diagonal)
        max_val=0
        for r in dp:
            max_val=max(max_val,max(r))
        return max_val**2
        