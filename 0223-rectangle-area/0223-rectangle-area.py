class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # this question is same as the Rectange Overlap
        # find the length * breadth for both traingle and find the intersection points and find the intersection area minus with sum of both rectangles 
        rec1 = (ax2-ax1)*(ay2-ay1)
        rec2 = (bx2-bx1)*(by2-by1)
        xOverlap = max(0,min(ax2,bx2) - max(ax1,bx1))
        yOverlap = max(0,min(ay2,by2) - max(ay1,by1))
        overlapArea = xOverlap * yOverlap
        totalArea= rec1+rec2-overlapArea
        return totalArea