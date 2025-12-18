class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # In this sliding window is wrong because of negative numbers
        # prefix[i] = sum of nums[0..i-1]
        # https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/editorial/#approach-1-priority-queue
        # refer this
        n=len(nums)
        cur_sum=0
        res=inf
        min_heap=[]
        for i in range(n):
            cur_sum+=nums[i]
            if cur_sum>=k:
                res=min(res,i+1) # already a subarray would be satisfy
            while min_heap and cur_sum-min_heap[0][0]>=k:
                val,end_index=heappop(min_heap)
                cur_len=i - end_index
                res=min(res,cur_len)
            heappush(min_heap,(cur_sum,i))
        return res if res!=inf else -1
