class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we can use the monotonic queue why because we can access in the two sides also 
        q=deque()
        l=0
        res=[]
        for r in range(len(nums)):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            if l>q[0]:
                q.popleft()
            if r-l+1>=k:
                res.append(nums[q[0]])
                l+=1
        return res
            