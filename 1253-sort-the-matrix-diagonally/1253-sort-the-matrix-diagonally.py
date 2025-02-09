class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        d={}
        for r in range(rows):
            for c in range(cols):
                if r-c in d:
                    heapq.heappush(d[r-c],mat[r][c])
                else:
                    d[r-c]=[]
                    heapq.heappush(d[r-c],mat[r][c])
        
        for r in range(rows):
            for c in range(cols):
                mat[r][c]=heapq.heappop(d[r-c])
        return mat