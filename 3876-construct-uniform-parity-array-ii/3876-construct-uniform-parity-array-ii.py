class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # refer this explanation -> https://leetcode.com/problems/construct-uniform-parity-array-ii/solutions/8498383/solution-by-la_castille-k6m8
        odd=all(n%2!=0 for n in nums1)
        even=all(n%2==0 for n in nums1)
        if odd or even:
            return True
        min_val=min(nums1)
        if min_val%2:
            return True
        return False