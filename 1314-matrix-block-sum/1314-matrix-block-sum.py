class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # [[1,2,3],
        #  [4,5,6],
        #  [7,8,9]]
        # [[0, 0, 0, 0], 
        #  [0, 1, 3, 6], 
        #  [0, 5, 12, 21], 
        #  [0, 12, 27, 45]]
        ROWS=len(mat)
        COLS=len(mat[0])
        pre_sum=[[0]*(COLS+1) for i in range(ROWS+1)]
        for r in range(ROWS):
            prefix=0
            for c in range(COLS):
                prefix+=mat[r][c]
                above=pre_sum[r][c+1]
                pre_sum[r+1][c+1]=prefix+above
        print(pre_sum)
        res=[[0]*(COLS) for i in range(ROWS)]
        for i in range(ROWS):
            for j in range(COLS):
                r1=max(0,i-k)
                c1=max(0,j-k)
                r2=min(ROWS-1,i+k)
                c2=min(COLS-1,j+k)
                bottomRight=pre_sum[r2+1][c2+1] # contains the whole sum 
                bottomLeft=pre_sum[r2+1][c1] # want to subtract this on the bottomRight
                topRight=pre_sum[r1][c2+1]  # want to subtract this on the bottomRight
                topLeft=pre_sum[r1][c1] # want to add this on the bottomRight because of two time we subtract the same value
                res[i][j]=bottomRight-bottomLeft-topRight+topLeft
        return res