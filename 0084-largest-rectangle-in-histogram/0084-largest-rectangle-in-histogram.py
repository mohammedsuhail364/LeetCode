class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # find next smaller element
        n=len(heights)
        def findNSE():
            stack=[]
            nse=[n]*n
            for i in range(len(heights)):
                while stack and heights[stack[-1]]>heights[i]:
                    idx=stack.pop()
                    nse[idx]=i
                stack.append(i)
            return nse
        def findPSEE(): # find the previous smaller or equal element
            stack=[]
            pse=[-1]*n
            for i in range(n):
                while stack and heights[stack[-1]]>heights[i]:
                    stack.pop()
                if stack:
                    pse[i]=stack[-1]
                stack.append(i)
            return pse
        nse=findNSE()
        pse=findPSEE()
        res=0
        for i in range(n):
            width=nse[i]-pse[i]-1
            height=heights[i]
            area=width*height
            res=max(res,area)
        return res
        