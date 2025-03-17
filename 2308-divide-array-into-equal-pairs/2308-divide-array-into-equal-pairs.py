class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        di=Counter(nums)
        for i in di:
            if di[i]%2!=0:
                return False
        return True