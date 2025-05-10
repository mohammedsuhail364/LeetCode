class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        val1=sum(nums1)+nums1.count(0)
        val2=sum(nums2)+nums2.count(0)
        if val1>val2 and not nums2.count(0) or val1<val2 and not nums1.count(0):
            return -1
        return max(val1,val2)
