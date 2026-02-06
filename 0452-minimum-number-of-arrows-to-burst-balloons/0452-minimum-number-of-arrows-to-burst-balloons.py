class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # refer neetcode
        points.sort()
        res=len(points) # for point we need a arrow if not intersect intervals
        prev=points[0]
        for i in range(1,len(points)):
            cur=points[i]
            # if merge occurs
            if prev[-1]>=cur[0]:
                res-=1
                prev=[cur[0],min(cur[-1],prev[-1])]
            else:
                prev=cur
        return res