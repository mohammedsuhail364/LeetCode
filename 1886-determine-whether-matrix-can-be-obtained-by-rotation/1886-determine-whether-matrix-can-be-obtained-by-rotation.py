from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        rotated=[[0]*n for _ in range(n)]
        for _ in range(4):
            for r in range(n):
                for c in range(n):
                    rotated[c][r]=mat[r][c]
            rotated=[rot[::-1] for rot in rotated]
            if rotated==target:
                return True
            mat=rotated
            rotated=[[0]*n for _ in range(n)]
        return False