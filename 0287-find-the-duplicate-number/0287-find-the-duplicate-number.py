class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # refer neetcode
        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        # slow pointer it is in the place of interaction
        slow2=0
        # we can move the slow2 pointer as well one 
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow
        