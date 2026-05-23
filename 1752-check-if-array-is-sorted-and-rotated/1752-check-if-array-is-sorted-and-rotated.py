class Solution:
    def check(self, nums: List[int]) -> bool:
        res=sorted(nums)
        if nums==res:
            return True
        for i in range(len(nums)): 
            nums.append(nums.pop(0))
            if nums==res:
                return True
        if nums==res:
                return True
        return False