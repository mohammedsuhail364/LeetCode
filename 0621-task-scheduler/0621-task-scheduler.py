class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # basically get the counts of each occurence and used after use put the deque for the pop first 
        q = deque()
        maxHeap = [c for c in Counter(tasks).values()]
        heapify_max(maxHeap)
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                count = heappop_max(maxHeap)
                currentCount = count - 1
                if currentCount:
                    q.append((currentCount,time+n))
            if q and q[0][1]==time:
                count,_ = q.popleft()
                heappush_max(maxHeap,count)
        return time