class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(r,c):
            if c==9:
                return backtrack(r+1,0)
            if r==9:
                return True
            if board[r][c]!='.':
                return backtrack(r,c+1)
            for num in map(str,range(1,10)):
                if num in row_val[r] or num in col_val[c] or num in sub_box[(r//3,c//3)]:
                    continue
                board[r][c]=num
                row_val[r].add(num)
                col_val[c].add(num)
                sub_box[(r//3,c//3)].add(num)
                if backtrack(r,c+1):
                    return True
                # backtrack the number
                board[r][c]='.'
                row_val[r].remove(num)
                col_val[c].remove(num)
                sub_box[(r//3,c//3)].remove(num)
            return False

        rows=len(board)
        cols=len(board[0])
        row_val=defaultdict(set)
        col_val=defaultdict(set)
        sub_box=defaultdict(set)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='.':
                    continue
                row_val[r].add(board[r][c])
                col_val[c].add(board[r][c])
                sub_box[(r//3,c//3)].add(board[r][c])
        
        backtrack(0,0)
                    


        