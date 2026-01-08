class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index={n:i for i,n in enumerate(nums2)}
        res=[-1]*len(nums1)
        for i in range(len(nums1)):
            idx=index[nums1[i]]
            for x in range(idx+1,len(nums2)):
                if nums2[idx]<nums2[x]:
                    res[i]=nums2[x]
                    break
        return res