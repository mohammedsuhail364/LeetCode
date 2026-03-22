from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        for _ in range(4):
            for r in range(n):
                for c in range(r,n):
                    mat[r][c],mat[c][r]=mat[c][r],mat[r][c]
            for row in mat:
                row.reverse()
            if mat==target:
                return True
        return False