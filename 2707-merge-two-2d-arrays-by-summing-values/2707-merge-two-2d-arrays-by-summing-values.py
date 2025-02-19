class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        di=defaultdict(int)
        for i,j in nums1:
            di[i]+=j
        for i,j in nums2:
            di[i]+=j
        res=[]
        for i,j in di.items():
            res.append([i,j])
        res.sort()
        return res