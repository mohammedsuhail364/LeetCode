class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        # strictly increasing prefix check
        inc_prefix = [True] * n
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                inc_prefix[i] = False
            else:
                inc_prefix[i] = inc_prefix[i-1]

        # strictly decreasing suffix check
        dec_suffix = [True] * n
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                dec_suffix[i] = False
            else:
                dec_suffix[i] = dec_suffix[i+1]

        ans = float('inf')
        for i in range(n-1):
            if inc_prefix[i] and dec_suffix[i+1]:
                left_sum = prefix_sum[i]
                right_sum = prefix_sum[-1] - prefix_sum[i]
                ans = min(ans, abs(left_sum - right_sum))

        return -1 if ans == float('inf') else ans