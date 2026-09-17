class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen={}
        for i in range(len(nums)-1):
            target = nums[i]+nums[i+1]
            if target in seen:
                return True
            
            seen[target]=seen.get(target,0)+1
        return False