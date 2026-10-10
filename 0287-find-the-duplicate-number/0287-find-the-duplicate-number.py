class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        # this is the place where find the intersection of two pointers
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        # set the another point in the start and consider that as a slow1 and run a single move to the both pointers we get the duplicate value
        slow1=nums[0]
        while slow != slow1:
            slow = nums[slow]
            slow1 = nums[slow1]
        return slow