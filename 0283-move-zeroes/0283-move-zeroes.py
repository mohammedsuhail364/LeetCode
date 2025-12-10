class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros=[]
        numbers=[]
        for i in nums:
            if i:
                numbers.append(i)
            else:
                zeros.append(i)
        numbers+=zeros
        for i in range(len(nums)):
            nums[i]=numbers[i]
        