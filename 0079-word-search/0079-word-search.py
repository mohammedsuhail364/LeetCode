class Solution:
    def exist(self, board, word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        def bfs(r,c,i):
            q=deque([(r,c,i)])
            visit=set([(r,c)])
            while q:
                row,col,w=q.popleft()
                if board[row][col]!=word[w]:
                    continue
                if w==len(word)-1:
                    return True
                for nr,nc in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visit and board[nr][nc]==word[w+1]:
                        q.append((nr,nc,w+1))
                        visit.add((nr,nc))
            return True if w==len(word) else False

        for r in range(rows):
            for c in range(cols):
                if board[r][c]==word[0]:
                    if bfs(r,c,0):
                        return True
        return False