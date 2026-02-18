class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS=len(board)
        COLS=len(board[0])
        row_set=defaultdict(set)
        col_set=defaultdict(set)
        box=defaultdict(set)
        for r in range(ROWS):
            for c in range(COLS):
                val=board[r][c]
                if board[r][c]!='.' and (val in row_set[r] or val in col_set[c] or val in box[(r//3,c//3)]):
                    return False

                if board[r][c]!='.':
                    row_set[r].add(val)
                    col_set[c].add(val)
                    box[(r//3,c//3)].add(val)
        return True
                