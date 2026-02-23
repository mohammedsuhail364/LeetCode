class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_set=defaultdict(set)
        col_set=defaultdict(set)
        sub_boxes=defaultdict(set)
        def dfs(idx):
            if idx==len(empties):
                return True
            r,c=empties[idx]
            for i in map(str,range(1,10)):
                if i not in row_set[r] and i not in col_set[c] and i not in sub_boxes[r//3,c//3]:
                    board[r][c]=i
                    row_set[r].add(i)
                    col_set[c].add(i)
                    sub_boxes[r//3,c//3].add(i)
                    if dfs(idx+1):
                        return True
                    board[r][c]='.'
                    row_set[r].remove(i)
                    col_set[c].remove(i)
                    sub_boxes[r//3,c//3].remove(i)
            return False
        empties=[]
        for r in range(9):
            for c in range(9):
                if board[r][c]!='.':
                    row_set[r].add(board[r][c])
                    col_set[c].add(board[r][c])
                    sub_boxes[r//3,c//3].add(board[r][c])
                else:
                    empties.append((r,c))
        dfs(0)
        