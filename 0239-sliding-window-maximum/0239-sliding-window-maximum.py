class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        q=deque() # stores index (easy to track the window)
        res=[]
        for r in range(len(nums)):
            # maintain the monotonic stack 
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            # maintain the window
            if l>q[0]:
                q.popleft()
            if (r+1)>=k: # found the window
                res.append(nums[q[0]])
                l+=1
        return res
