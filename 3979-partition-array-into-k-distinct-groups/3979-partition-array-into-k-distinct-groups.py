class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        freq=Counter(nums)
        if len(nums)%k!=0:
            return False
        groups=len(nums)//k
        for j in freq.values():
            if j>groups:
                return False
        return True
