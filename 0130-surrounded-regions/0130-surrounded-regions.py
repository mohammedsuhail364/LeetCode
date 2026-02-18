class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r,c):
            if r<0 or r==ROWS or c<0 or c==COLS or board[r][c]!='O':
                return
            board[r][c]='T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            
        ROWS=len(board)
        COLS=len(board[0])
        # convert 'O' into 'T' we can first mark the not surrounded one then we can easily mark the surrounded ones
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='O' and (r==0 or r==ROWS-1 or c==0 or c==COLS-1):
                    dfs(r,c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]!='T':
                    board[r][c]='X' 
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='T':
                    board[r][c]='O' 
        
