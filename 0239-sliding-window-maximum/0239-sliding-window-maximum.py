class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=r=0
        output=[]
        q=deque()
        for r in range(len(nums)):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            if l>q[0]:
                q.popleft()
            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
        return output