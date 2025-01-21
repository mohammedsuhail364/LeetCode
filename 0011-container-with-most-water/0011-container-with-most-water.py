class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Start With two pointer
        l,r=0,len(height)-1
        res=0
        while l<r:
            maxArea=(r-l)*min(height[l],height[r])
            res=max(res,maxArea)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res