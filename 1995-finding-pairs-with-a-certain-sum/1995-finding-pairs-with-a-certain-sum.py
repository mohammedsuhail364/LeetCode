class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1=nums1
        self.nums2=nums2
        self.count_map=defaultdict(int)
        for j in self.nums2:
            self.count_map[j]+=1
    def add(self, index: int, val: int) -> None:
        old_val=self.nums2[index]
        self.count_map[old_val]-=1
        new_val=old_val+val
        self.nums2[index]=new_val
        self.count_map[new_val]+=1
    def count(self, tot: int) -> int:
        res=0
        for i in self.nums1:
            rem=tot-i
            res+=self.count_map[rem]
        return res
# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)