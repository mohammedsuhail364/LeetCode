class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set=set()
        res=float('inf')
        for i in points:
            points_set.add(tuple(i))
        for i in range(len(points)):
            x1,y1=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                # to find diagonal of (x1,y1) -> to check not in same row or same coloumn
                if x1!=x2 and y1 !=y2:
                    # to check alternating points are in the points_set to make the rectange
                    if (x1,y2) in points_set and (x2,y1) in points_set:
                        # to find the length and breadth
                        area=abs(x1-x2) * abs(y1-y2)
                        res=min(res,area)
        return res if res!= float('inf') else 0