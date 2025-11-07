class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_val=deque()
        min_val=deque()
        l=0
        res=0
        for r in range(len(nums)):
            while max_val and nums[r]>max_val[-1]:
                max_val.pop()
            while min_val and nums[r]<min_val[-1]:
                min_val.pop()
            max_val.append(nums[r])
            min_val.append(nums[r])
            while max_val[0]-min_val[0]>limit and l<r:
                if max_val[0]==nums[l]:
                    max_val.popleft()
                if min_val[0]==nums[l]:
                    min_val.popleft()
                l+=1
            res=max(res,r-l+1)
        return res