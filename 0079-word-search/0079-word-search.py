class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS=len(board)
        COLS=len(board[0])
        board_count=Counter()
        for row in board:
            board_count+=Counter(row)
        word_count=Counter(word)
        for ch in word:
            if word_count[ch]>board_count[ch]:
                return False
        if word_count[word[0]]>word_count[word[-1]]:
            word=word[::-1]
        def dfs(r,c,i):
            if i>=len(word):
                return True
            if r==ROWS or r<0 or c==COLS or c<0:
                return False
            if board[r][c]!=word[i]:
                return False

            temp = board[r][c]
            board[r][c] = "#"   # mark as visited
            res= (
            dfs(r+1,c,i+1) or 
            dfs(r-1,c,i+1) or 
            dfs(r,c+1,i+1) or 
            dfs(r,c-1,i+1)
            )
            board[r][c]=temp
            return res
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False