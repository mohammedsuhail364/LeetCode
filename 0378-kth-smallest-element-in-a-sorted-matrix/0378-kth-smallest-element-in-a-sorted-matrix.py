class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def countLessElements(m):
            # this one similiar to search matrix II
            r=n-1 # start with bottom left
            c=0
            count=0
            while r>=0 and c<n:
                if matrix[r][c]<=m:
                    count+=(r+1)
                    c+=1 # move to next column
                else:
                    r-=1 # right side are all bigger elements
            return count
        n=len(matrix)
        # we know first element is lowest one
        l=matrix[0][0]
        # we know last element is highest one due to the row wise sorted and column wise sorted
        r=matrix[n-1][n-1]
        res=r # possible answer
        while l<=r:
            m=(l+r)//2
            # we can check m is our guess if we have minimum lesser k values than m then m is also one of our res
            if countLessElements(m)>=k:
                res=m
                r=m-1
            else: # this is not our res so we can check higher elements
                l=m+1
        return res 