class Solution:
    def trap(self, height: List[int]) -> int:
        # find the left max
        n=len(height)
        left_max=[0]*n
        right_max=[0]*n
        left_max[0]=height[0]
        for i in range(1,len(height)):
            left_max[i]=max(left_max[i-1],height[i])
        right_max[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            right_max[i]=max(right_max[i+1],height[i])
        water=0
        for i in range(n):
            if height[i]<left_max[i] and height[i]<right_max[i]: # that time only water store in that place
                water+=(min(left_max[i],right_max[i])-height[i])
        return water