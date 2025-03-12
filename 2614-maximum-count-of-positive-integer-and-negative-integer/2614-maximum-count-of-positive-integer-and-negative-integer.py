class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        ne=0
        po=0
        for i in nums:
            if i>0:
                po+=1
            elif i<0:
                ne+=1
        return max(ne,po)