class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        nums.sort(key=lambda x:abs(x),reverse=True)
        res=nums[0]*nums[1]
        if res<0:
            return res*-10**5
        return res*10**5