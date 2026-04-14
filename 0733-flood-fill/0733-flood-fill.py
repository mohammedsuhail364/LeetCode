class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target=image[sr][sc]
        def bfs(row,col):
            q=deque([(row,col)])
            
            while q:
                r,c=q.popleft()
                for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if nr>=0 and nr<len(image) and nc>=0 and nc<len(image[0]) and image[nr][nc]==target:
                        q.append((nr,nc))
                        image[nr][nc]="T"
        image[sr][sc]="T"
        bfs(sr,sc)
        ROWS=len(image)
        COLS=len(image[0])
        for r in range(ROWS):
            for c in range(COLS):
                if image[r][c]=="T":
                    image[r][c]=color
        return image