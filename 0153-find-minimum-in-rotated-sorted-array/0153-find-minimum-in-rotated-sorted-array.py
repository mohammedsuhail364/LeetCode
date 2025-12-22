class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Solution Approach
        # We use the standard binary search template to find the first index where nums[i] <= nums[n-1] is true.

        # Initial Setup:

        # left, right = 0, len(nums) - 1
        # first_true_index = -1
        # Initialize the search boundaries and a variable to track the first position where the feasible condition is true.

        # Feasible Function: For any index mid, the feasible condition is: nums[mid] <= nums[n-1]

        # This creates a pattern like [false, false, false, true, true, true] where we want to find the first true.

        # Binary Search Loop: Using while left <= right:

        # Calculate the middle index: mid = (left + right) // 2

        # Check if feasible (nums[mid] <= nums[n-1]):

        # If true: This could be the minimum or the minimum could be further left. Record first_true_index = mid, then search left with right = mid - 1
        # If false: The minimum must be to the right. Search right with left = mid + 1
        # Return Result: After the loop, first_true_index holds the index of the minimum element. Return nums[first_true_index].

        # Edge Case: If the array is not rotated (or rotated n times), the entire array satisfies the feasible condition, so first_true_index will be 0, correctly returning the first element.

        # Time Complexity: O(log n) - We eliminate half of the search space in each iteration. Space Complexity: O(1) - We only use a constant amount of extra space for the pointers.
        l=0
        r=len(nums)-1
        first_true_index=-1
        while l<=r:
            m=(l+r)//2
            if nums[m]<=nums[-1]:
                # we identify this is one of the answer we can check the left part also
                first_true_index = m
                r=m-1
            else:
                l=m+1
        return nums[first_true_index]