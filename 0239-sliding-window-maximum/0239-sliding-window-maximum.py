class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        q=deque()
        res=[]
        for r in range(len(nums)):
            # maintain the monotonic stack
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            # remove the non valid left pointers  
            if q and l>q[0]:
                q.popleft()
            q.append(r)
            if (r-l+1)>=k:
                res.append(nums[q[0]])
                l+=1
        return res