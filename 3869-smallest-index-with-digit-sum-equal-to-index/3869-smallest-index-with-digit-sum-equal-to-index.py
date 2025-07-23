class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def made_single_digit(num):
            res=0
            while num:
                res+=num%10
                num//=10
            return res
        for i in range(len(nums)):
            num=made_single_digit(nums[i])
            if num==i:
                return i
        return -1