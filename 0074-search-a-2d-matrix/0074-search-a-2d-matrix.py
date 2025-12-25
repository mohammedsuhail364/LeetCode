class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        l=0
        r=len(matrix)-1
        while l<=r:
            m=(l+r)//2
            for x in matrix[m]:
                if x==target:
                    return True
            if matrix[m][0]>target:
                r=m-1
            else:
                l=m+1
        return False