class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows=len(mat)
        cols=len(mat[0])
        ele=defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                val=r+c
                ele[val].append(mat[r][c])
        res=[]
        for i in range(rows+cols-1):
            if i%2:
                res+=ele[i]
            else:
                res+=(ele[i][::-1])
        return res