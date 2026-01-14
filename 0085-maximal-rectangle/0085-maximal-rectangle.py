class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights: List[int]) -> int:
            # refer neetcode
            n=len(heights)
            max_area=0
            stack=[]
            for i in range(n):
                start=i
                while stack and stack[-1][-1]>heights[i]: # that means top of the stack is invalid it cannot move further we can calculate the res for the top of the stack
                    idx,h=stack.pop()
                    max_area=max(max_area,h*(i-idx)) # refers width
                    start=idx # this line tells current index is start at the idx why ? because heights[idx]>heights[i] so possibly it can extend left also that is the indication
                stack.append((start,heights[i]))
            for i,h in stack:
                max_area=max(max_area,h*(n-i)) # refers width
            return max_area
        # refer this 84. Largest Rectangle in Histogram
        # same logic used here
        heights=[0]*len(matrix[0])
        res=0
        for row in matrix:
            for c in range(len(row)):
                if row[c]=='1':
                    heights[c]+=1
                else:
                    heights[c]=0
            res=max(res,largestRectangleArea(heights))
        return res
                