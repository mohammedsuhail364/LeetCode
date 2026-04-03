class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=[i for i in nums if not i ]
        nonZero=[i for i in nums if i ]

        temp=nonZero+zero
        for n in range(len(nums)):
            nums[n]=temp[n]