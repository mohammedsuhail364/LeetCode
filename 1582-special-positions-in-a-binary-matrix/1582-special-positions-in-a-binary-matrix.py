class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def check(r,c):
            for col in range(len(mat[r])):
                if col!=c and mat[r][col]:
                    return False
            for row in range(len(mat)):
                if mat[row][c] and row!=r:
                    return False
            return True 
        res=0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c]==0:
                    continue
                if check(r,c):
                    res+=1
        return res
        