class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in hashMap:
                return [hashMap[complement],i]
            hashMap[nums[i]]=i
