class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # refer tech dose
        n=len(startTime)
        if eventTime>endTime[-1]:
            startTime.append(eventTime)
            endTime.append(eventTime)
            n+=1
        win_size=0
        max_size=0
        last_end=0
        q=deque()
        for pos in range(n):
            win_size+=(startTime[pos]-last_end)
            q.append(startTime[pos]-last_end)
            max_size=max(max_size,win_size)
            if len(q)>k:
                win_size-=q.popleft()
            last_end=endTime[pos]
        return max_size