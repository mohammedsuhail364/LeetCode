from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre_sum=[[0] for i in range(len(matrix))]
        for r,row in enumerate(matrix):
            pre=self.pre_sum[r]
            for n in row:
                pre.append(pre[-1]+n)
# [[0, 3, 3, 4, 8, 10], 
#  [0, 5, 11, 14, 16, 17], 
#  [0, 1, 3, 3, 4, 9], 
#  [0, 4, 5, 5, 6, 13], 
#  [0, 1, 1, 4, 4, 9]]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res=0
        while row1<=row2:
            start=self.pre_sum[row1]
            res+=start[col2+1]-start[col1]
            row1+=1
        return res
        

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)