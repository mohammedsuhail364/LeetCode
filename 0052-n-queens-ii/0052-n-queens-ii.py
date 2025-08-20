class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res=0
        board=[['.']*n for i in range(n)]
        cols=set()
        neg_diag=set()
        pos_diag=set()
        def backtrack(r):
            if r==n:
                self.res+=1
                return 
            for c in range(n):
                if c not in cols and (r-c) not in neg_diag and (r+c) not in pos_diag:
                    cols.add(c)
                    neg_diag.add(r-c)
                    pos_diag.add(r+c)
                    board[r][c]="Q"
                    backtrack(r+1)
                    cols.remove(c)
                    neg_diag.remove(r-c)
                    pos_diag.remove(r+c)
                    board[r][c]="."
        backtrack(0)
        return self.res