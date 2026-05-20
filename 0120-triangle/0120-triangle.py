class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS=len(triangle)
        cache={}
        def dfs(r,c):
            if (r,c) in cache:
                return cache[r,c]
            if r>=ROWS:
                return inf
            if c<0 or c>=len(triangle[r]):
                return inf
            if r==ROWS-1:
                return triangle[r][c]
            cache[r,c] = triangle[r][c]+min(dfs(r+1,c+1),dfs(r+1,c))
            return cache[r,c]
        return dfs(0,0)