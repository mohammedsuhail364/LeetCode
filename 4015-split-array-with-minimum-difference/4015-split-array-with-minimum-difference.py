class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n=len(nums)
        prefix_sum=[0]*n
        prefix_sum[0]=nums[0]
        for i in range(1,n):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
        is_increase=[True]*n
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                is_increase[i]=is_increase[i-1]
            else:
                is_increase[i]=False
        is_decrease=[True]*n
        for i in range(n-2,-1,-1):
            if nums[i]>nums[i+1]:
                is_decrease[i]=is_decrease[i+1]
            else:
                is_decrease[i]=False
        res=inf
        for i in range(n-1):
            if is_increase[i] and is_decrease[i+1]:
                left=prefix_sum[i]
                right=prefix_sum[-1]-prefix_sum[i]
                res=min(res,abs(left-right))
        return -1 if res==inf else res