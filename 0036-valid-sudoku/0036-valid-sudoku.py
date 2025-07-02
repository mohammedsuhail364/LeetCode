class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        col=defaultdict(set)
        sub_box=defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=='.':
                    continue
                value=board[r][c]
                if value in row[r] or value in col[c] or value in sub_box[(r//3,c//3)]:
                    return False
                row[r].add(value)
                col[c].add(value)
                sub_box[(r//3,c//3)].add(value)
        return True