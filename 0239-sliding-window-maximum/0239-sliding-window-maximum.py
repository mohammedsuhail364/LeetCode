class Solution:
    def maxSlidingWindow(self, nums, k: int):
        q=deque()
        l=0
        res=[]
        for r in range(len(nums)):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            while l>q[0]:
                q.popleft()
            if (r+1)>=k:
                res.append(nums[q[0]])
                l+=1
            
        return res