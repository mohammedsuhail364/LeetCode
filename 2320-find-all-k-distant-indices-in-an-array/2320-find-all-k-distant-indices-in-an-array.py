class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res=set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i-j)<=k and nums[j]==key:
                    res.add(i)
        return sorted(list(res))