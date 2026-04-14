class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        islands=0
        visited=set()
        def bfs(row,col):
            q=deque([(row,col)])
            visited.add((row,col))
            while q:
                r,c=q.popleft()
                for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if nr>=0 and nr<ROWS and nc>=0 and nc<COLS and (nr,nc) not in visited and grid[nr][nc]=="1":
                        q.append((nr,nc))
                        visited.add((nr,nc))
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands