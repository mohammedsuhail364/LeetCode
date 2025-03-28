class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # refer neetcode
        rows=len(grid)
        cols=len(grid[0])
        q=[(n,i) for i,n in enumerate(queries)]
        q.sort()
        res=[0]*len(queries)
        min_heap=[(grid[0][0],0,0)]
        visit=set([(0,0)])
        points=0
        for limit , index in q:
            while min_heap and min_heap[0][0]<limit:
                val,r,c=heapq.heappop(min_heap)
                points+=1
                for nr,nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visit :
                        heapq.heappush(min_heap,(grid[nr][nc],nr,nc))
                        visit.add((nr,nc))
            res[index]=points
        return res
