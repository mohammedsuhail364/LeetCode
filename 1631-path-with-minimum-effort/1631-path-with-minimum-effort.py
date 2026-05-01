class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS=len(heights)
        COLS=len(heights[0])
        min_heap=[(0,0,0)]
        max_effort=0
        visit=set()
        while min_heap:
            e,r,c=heappop(min_heap)
            max_effort=max(e,max_effort)
            if (r,c)==(ROWS-1,COLS-1):
                return max_effort
            visit.add((r,c))
            for nr,nc in [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]:
                if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visit:
                    new_effort=abs(heights[r][c]-heights[nr][nc])
                    heappush(min_heap,(new_effort,nr,nc))
        return -1
