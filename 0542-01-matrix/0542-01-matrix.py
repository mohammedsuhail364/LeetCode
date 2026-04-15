class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        this is classic multisource bfs problem the main purpose of this problem is to find the nearest 0 , if the cell is already a zero so the answer is 0 else we want search layer by layer 
        """
        ROWS=len(mat)
        COLS=len(mat[0])
        q=deque()
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c]==0:
                    q.append((r,c)) # we dont do anything same value
                else:
                    mat[r][c]=inf # because we want to say this want to be calculate the nearest 0
        while q:
            r,c=q.popleft()
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=nr<ROWS and 0<=nc<COLS and mat[nr][nc]==inf:
                    q.append((nr,nc))
                    mat[nr][nc]=mat[r][c]+1
        return mat