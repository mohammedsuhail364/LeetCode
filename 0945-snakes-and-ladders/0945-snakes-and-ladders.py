class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length=len(board)
        board.reverse()
        def intToPos(square):
            r=(square-1)//length
            c=(square-1)%length
            if r%2:
                c=length-1-c
            return [r,c]
        q=deque()
        q.append([1,0]) # square,moves
        visit=set()
        visit.add(1)
        while q:
            square,moves=q.popleft()
            for i in range(1,7):
                next_square=square+i
                r,c=intToPos(next_square)
                if board[r][c]!=-1:
                    next_square=board[r][c]
                if next_square==length**2:
                    return moves+1
                if next_square not in visit:
                    visit.add(next_square)
                    q.append([next_square,moves+1])
        return -1
