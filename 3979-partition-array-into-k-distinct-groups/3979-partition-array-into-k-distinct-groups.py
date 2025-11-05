class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        freq=Counter(nums)
        if len(nums)%k!=0:
            return False
        groups=len(nums)//k
        for i,j in freq.items():
            if j>groups:
                return False
        return True
