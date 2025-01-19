class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft=0
        maxLeftArr=[]
        ans=0
        for i in range(len(height)):
            maxLeftArr.append(maxLeft)
            if height[i]>maxLeft:
                maxLeft=height[i]
        print(maxLeftArr)  
        maxRight=0
        maxRightArr=[]
        for i in range(len(height)-1,-1,-1):
            maxRightArr.append(maxRight)
            if height[i]>maxRight:
                maxRight=height[i]
        print(maxRightArr) 
        maxRightArr=maxRightArr[::-1]
        for i in range(len(height)):
            val =min(maxLeftArr[i],maxRightArr[i])-height[i]
            if val>0:
                ans+=val
        return ans
            