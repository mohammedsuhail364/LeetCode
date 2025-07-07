class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # refer tech dose
        events.sort()
        i=0
        min_heap=[]
        day=1
        n=len(events)
        res=0
        while i<n or min_heap:
            # add events occur on same day
            while i<n and events[i][0]==day:
                heappush(min_heap,events[i][1])
                i+=1
            # remove expired events
            while min_heap and min_heap[0]<day:
                heappop(min_heap)
            # add res for once a event in day
            if min_heap:
                heappop(min_heap)
                res+=1
            day+=1
        return res