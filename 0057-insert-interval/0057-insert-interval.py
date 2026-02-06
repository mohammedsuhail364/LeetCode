class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # first find the intersection point for new intervel
        res=[]
        i=0
        n=len(intervals)
        while i<n and intervals[i][1]<newInterval[0]:
            res.append(intervals[i])
            i+=1
        # this is the point we want to intersect but also we want to merge the intervals when we insert
        while i<n and intervals[i][0]<=newInterval[1]:
            newInterval[0]=min(intervals[i][0],newInterval[0])
            newInterval[1]=max(intervals[i][1],newInterval[1])
            i+=1
        res.append(newInterval)
        while i<n:
            res.append(intervals[i])
            i+=1
        return res
