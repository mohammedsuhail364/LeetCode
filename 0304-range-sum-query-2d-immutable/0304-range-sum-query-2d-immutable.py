from typing import List
class NumMatrix:
    # refer neetcode and see this code if you dont understand
    def __init__(self, matrix: List[List[int]]):
        ROWS=len(matrix)
        COLS=len(matrix[0])
        self.pre_sum=[[0]*(COLS+1) for i in range(ROWS+1)]
        for r in range(ROWS):
            prefix=0
            for c in range(COLS):
                prefix+=matrix[r][c]
                above=self.pre_sum[r][c+1]
                self.pre_sum[r+1][c+1]=prefix+above
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        r1,c1,r2,c2=row1+1,col1+1,row2+1,col2+1
        bottomRight=self.pre_sum[r2][c2]
        topLeft=self.pre_sum[r1-1][c1-1]
        topRight=self.pre_sum[r1-1][c2]
        bottomLeft=self.pre_sum[r2][c1-1]
        ans=bottomRight-bottomLeft-topRight+topLeft
        return ans
        

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)