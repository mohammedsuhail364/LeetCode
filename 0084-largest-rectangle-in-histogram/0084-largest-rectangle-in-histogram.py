class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        res=0
        n=len(heights)
        for i in range(len(heights)):
            start=i
            while stack and stack[-1][-1]>heights[i]: # this line indicates stack[-1][-1] is invalid after our current heights[i] because it cannot extend due to our heights[i] is lesser than this so we can pop that and find their value
                idx,h=stack.pop()
                res=max(res,(i-idx)*h) # (i-idx) refers to width
                start=idx # this line indicates our heights[i]'s left boundary is extend due to the higher value of stack[-1][-1]
            # final calculation if stack is non empty
            stack.append((start,heights[i]))
        for idx,h in stack:
            res=max(res,(n-idx)*h)
            
        return res