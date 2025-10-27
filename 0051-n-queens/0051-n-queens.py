class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[['.']*n for i in range(n)] 
        cols=set()
        pos_diagonal=set()
        neg_diagonal=set()
        def dfs(r,c):
            if r==n:
                res.append([''.join(x) for x in board])
                return
            for c in range(n):
                if c not in cols and (r-c) not in neg_diagonal and (r+c) not in pos_diagonal:
                    board[r][c]='Q'
                    cols.add(c)
                    neg_diagonal.add(r-c)
                    pos_diagonal.add(r+c)
                    dfs(r+1,c)
                    board[r][c]='.'
                    cols.remove(c)
                    neg_diagonal.remove(r-c)
                    pos_diagonal.remove(r+c)
        dfs(0,0)
        return res