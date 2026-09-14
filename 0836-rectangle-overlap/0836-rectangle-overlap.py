class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # this question is basically find the intersection of the area between the corner points if it was greater than zero means this is overlap else non overlap
        # to find the four corners of the intersection points 
        x1,y1,x2,y2 = rec1
        x3,y3,x4,y4 = rec2
        xOverlap = max(0,min(x2,x4) - max(x1,x3))
        yOverlap = max(0,min(y2,y4) - max(y1,y3))
        area = xOverlap * yOverlap
        print(area)
        return True if area else False