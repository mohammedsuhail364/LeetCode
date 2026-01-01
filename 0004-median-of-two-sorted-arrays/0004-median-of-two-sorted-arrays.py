class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # refer take You forward
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        n=len(nums1)
        m=len(nums2)
        total=n+m+1
        l=0
        r=n # smaller array length
        while l<=r:
            i=(l+r)//2 # cutting part in nums1
            j=(n+m+1)//2-i # refers remaining element from removing "i"
            aLeft=nums1[i-1] if i>0 else -inf # if no array try to assume the very low value
            aRight=nums1[i] if i<n else inf #if no array try to assume large value
            bLeft=nums2[j-1] if j>0 else -inf
            bRight=nums2[j] if j<m else inf
            if aLeft<=bRight and bLeft<=aRight: # valid sorted array
                if (m+n)%2: # odd length
                    return max(aLeft,bLeft)
                else: # even length
                    return (max(aLeft,bLeft)+min(aRight,bRight))/2
            # remove one part 
            elif aLeft>bRight: # move the right pointer because we can take 4 elements in the nums1 but it is not correct then 5,6,7 from nums1 is not correct so move the right pointer
                r=i-1
            else:
                l=i+1
        

