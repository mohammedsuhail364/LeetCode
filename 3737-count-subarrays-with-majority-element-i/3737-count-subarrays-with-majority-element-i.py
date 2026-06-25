class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        res=0
        for i in range(len(nums)):
            cur=0
            for j in range(i,len(nums)):
                cur+=(nums[j]==target)
                half=(j-i+1)//2
                res+=(cur>half)
        return res