class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        """
        this one is tricky problem and basic intuation is we want to find the area of the triangle with given points the basic formula is => 1/2 * base * height
        => vector of AB = (x2-x1,y2-y1)
        => vector of AC = (x3-x1,y3-y1)
        => |AB x AC|=|(x2-x1)(y3-y1)-(x3-x1)(y2-y1)| -> it is formula of parallogram
        => | x2y3 - x2y1 - x1y3 + x1y1 - x3y2 + x3y1 + x1y2 - x1y1 |
        => grouping them
        => | x1(y2-y3) + x2(y3-y1) + x3(y1-y2) |
        => triangle is always half of parallogram
        => 1/2 * | x1(y2-y3) + x2(y3-y1) + x3(y1-y2) | 
        we can brute force it to find the max area  
        """
        max_area=0
        for i in range(len(points)):
            x1,y1=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                for k in range(j+1,len(points)):
                    x3,y3=points[k]
                    area=1/2 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
                    max_area=max(area,max_area)
        return max_area