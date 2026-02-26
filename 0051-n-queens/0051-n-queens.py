class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for i in range(n)]
        res=[]
        cols=set()
        pos_diag=set()
        neg_diag=set()
        def dfs(r):
            if r==n:
                temp=[''.join(v) for v in board]
                res.append(temp)
                return
            for c in range(n):
                if c not in cols and (r-c) not in neg_diag and (r+c) not in pos_diag:
                    board[r][c]='Q'
                    cols.add(c)
                    neg_diag.add(r-c)
                    pos_diag.add(r+c)
                    dfs(r+1)
                    board[r][c]='.'
                    cols.remove(c)
                    neg_diag.remove(r-c)
                    pos_diag.remove(r+c)

        dfs(0)
        return res