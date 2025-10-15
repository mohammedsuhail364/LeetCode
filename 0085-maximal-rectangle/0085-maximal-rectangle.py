class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleInHistogram(heights):
            max_area=0
            stack=[]
            n=len(heights)
            for i in range(n):
                start=i
                while stack and stack[-1][-1]>heights[i]:
                    index,height=stack.pop()
                    max_area=max(max_area,height*(i-index))
                    start=index
                stack.append((start,heights[i]))
            for i,h in stack:
                max_area=max(max_area,h*(n-i))
            return max_area
        rows,cols=len(matrix),len(matrix[0])
        heights=[0]*cols
        res=0
        for row in matrix:
            for c in range(cols):
                if row[c]=='1':
                    heights[c]+=1
                else:
                    heights[c]=0
            res=max(res,largestRectangleInHistogram(heights))
        return res