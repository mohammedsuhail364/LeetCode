class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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