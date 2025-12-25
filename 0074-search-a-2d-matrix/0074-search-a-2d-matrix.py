class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        def is_same(mid):
            nums=matrix[mid]
            l=0
            r=len(nums)-1
            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    return True
                elif nums[m]>target:
                    r=m-1
                else:
                    l=m+1
            return False
        l=0
        r=len(matrix)-1
        while l<=r:
            m=(l+r)//2
            if is_same(m):
                return True
            if matrix[m][0]>target:
                r=m-1
            else:
                l=m+1
        return False