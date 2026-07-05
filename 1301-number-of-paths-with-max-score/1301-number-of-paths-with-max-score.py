class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        # this question basically a DP Problem just to check the path 
        ROWS=len(board)
        COLS=len(board[0])
        memo={}
        MOD=10**9+7
        def dfs(r,c):
            if (r,c)==(0,0): # base reached E
                return (0,1) # base case we reached the E so we return (0,1) 0 -> sum 1 -> ways 
            if c<0 or r<0 or board[r][c]=="X":
                return (-1,0) # there is no path after this
            if (r,c) in memo:
                return memo[r,c]
            best_sum=-1
            ways=0
            for nr,nc in [(r-1,c),(r,c-1),(r-1,c-1)]:
                if nr<0 or nc < 0:
                    continue
                sub_sum,sub_ways=dfs(nr,nc)
                if sub_sum==-1:
                    continue  # that neighbor leads nowhere
                if sub_sum>best_sum: # when we see the max sum so we can change the best sum and ways also 
                    best_sum=sub_sum
                    ways=sub_ways
                elif sub_sum==best_sum:
                    ways=(ways+sub_ways)%MOD
            if best_sum==-1:
                memo[r,c] = (-1,0)
                return memo[r,c]
            digit=0 if board[r][c]=="S" else int(board[r][c])
            res=(best_sum+digit,ways)
            memo[r,c] = res
            return res

        best_sum,ways=dfs(ROWS-1,COLS-1)
        if best_sum==-1:
            return [0,0]
        return [best_sum,ways]