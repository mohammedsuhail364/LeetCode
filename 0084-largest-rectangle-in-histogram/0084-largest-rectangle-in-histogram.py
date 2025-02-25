class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        max_area=0
        for i in range(n):
            start=i
            while stack and stack[-1][1]>heights[i]:
                index,height=stack.pop()
                max_area=max(max_area,height*(i-index))
                start=index
            stack.append((start,heights[i]))
        for i,h in stack:
            max_area=max(max_area,h*(n-i))
        return max_area