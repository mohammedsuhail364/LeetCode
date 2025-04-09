class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k>min(nums):
            return -1
        unique_elements=set(nums)
        if k in unique_elements:
            return len(unique_elements)-1
        return len(unique_elements)