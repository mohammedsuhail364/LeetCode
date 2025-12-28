class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # partial optimized 
        # as we know this is sorted so we can find the first negative then we can calculate easily other negatives
        def find_first_negative(nums):
            l=0
            r=len(nums)-1
            res=-1
            while l<=r:
                m=(l+r)//2
                if nums[m]<0:
                    res=m
                    r=m-1
                else:
                    l=m+1
            return res
        n,m=len(grid),len(grid[0])
        res=0
        for r in range(n):
            tmp=find_first_negative(grid[r])
            if tmp!=-1:
                res+=(m-tmp)
        return res

        # brute force O(n*m)
        # res=0
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c]<0:
        #             res+=1
        # return res
        