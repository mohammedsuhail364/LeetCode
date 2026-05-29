class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sum_of_digits(n):
            res=0
            while n:
                res+=n%10
                n=n//10
            return res
        for n in range(len(nums)):
            nums[n]=sum_of_digits(nums[n])
        return min(nums)