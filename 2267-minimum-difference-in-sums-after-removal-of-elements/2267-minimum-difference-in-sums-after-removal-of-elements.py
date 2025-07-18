class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        total_len=len(nums)
        n=total_len//3
        right_sum=0
        right_prefix_sum=[0]*total_len
        min_heap=[]
        for i in range(total_len-1,n-1,-1):
            right_sum+=nums[i]
            heappush(min_heap,nums[i])
            if len(min_heap)>n:
                right_sum-=heappop(min_heap)
            if len(min_heap)==n:
                right_prefix_sum[i]=right_sum
        left_sum=0
        max_heap=[]
        min_diff=inf
        for i in range(2*n):
            left_sum+=nums[i]
            heappush(max_heap,-nums[i])
            if len(max_heap)>n:
                left_sum-= -heappop(max_heap)
            if len(max_heap)==n:
                min_diff=min(min_diff,left_sum-right_prefix_sum[i+1])
        return min_diff