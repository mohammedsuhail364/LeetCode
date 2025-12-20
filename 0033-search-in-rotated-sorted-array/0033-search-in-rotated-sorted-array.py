class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return m
            # we can only check in the sorted position 
            # first we can check if the left side is sorted or not
            if nums[l]<=nums[m]:
                # we can check the target is in the left side
                if nums[l]<=target<nums[m]:
                    r=m-1 # move the right pointer to mid - 1 and check
                else:
                    # in this time we know target is not in the left side so we can move the left pointer to mid+1
                    l=m+1 
            else:
                # we can identify the right is sorted
                if nums[m]<target<=nums[r]: # we can check the target is in the right side
                    l=m+1
                else:
                    r=m-1
        return -1