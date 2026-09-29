class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # refer take you forward 
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        # always nums1 as smallest because we can do binary search in this array with this array we can find the remaining elements in the nums2
        n=len(nums1)
        m=len(nums2)
        total=n+m+1 # why because of plus 1 is always left has more element than right side if the array length is odd even means both side length are equal
        l=0
        r=n
        while l<=r:
            i = (l+r)//2 
            j = (total//2) - i
            l1 = nums1[i-1] if i>0 else -inf
            r1 = nums1[i] if i<n else inf
            l2 = nums2[j-1] if j>0 else -inf
            r2 = nums2[j] if j<m else inf
            if l1<=r2 and l2<=r1:
                if (m+n)%2:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
            elif l1>r2:
                r=i-1
            else:
                l=i+1
