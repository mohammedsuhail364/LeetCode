from typing import List
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        for r in range(len(boxGrid)):
            n=len(boxGrid[r])
            for c in range(n-1,-1,-1):
                x=c+1
                while x<n and boxGrid[r][x]==".":
                    x+=1
                if x-1<n and boxGrid[r][c]=="#" and boxGrid[r][x-1]==".":
                   boxGrid[r][c],boxGrid[r][x-1] = boxGrid[r][x-1],boxGrid[r][c] 
        n=len(boxGrid)
        m=len(boxGrid[0])

        transpose=[[0]*n for j in range(m)]
        for i in range(m):
            for j in range(n):
                transpose[i][j]=boxGrid[j][i]
        for row in transpose:
            row.reverse()
        return transpose
