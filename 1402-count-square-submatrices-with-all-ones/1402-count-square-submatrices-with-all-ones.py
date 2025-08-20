class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def is_valid(i,j,x):
            for r in range(i,i+x):
                for c in range(j,j+x):
                    if not matrix[r][c]:
                        return False
            return True
        res=0
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                res+=matrix[i][j]
                x=2
                while i+x<=rows and j+x<=cols:
                    if is_valid(i,j,x):
                        res+=1
                    else:
                        break
                    x+=1
        return res

            
                    