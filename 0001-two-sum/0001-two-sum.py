class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache={}
        for n in range(len(nums)):
            rem=target-nums[n]
            if rem in cache:
                return [cache[rem],n]
            cache[nums[n]]=n
        return []