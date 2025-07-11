from heapq import heappop,heappush
from collections import defaultdict
class Solution:
    def mostBooked(self, n: int, meetings) -> int:
        # try to solve brute force first
        meetings.sort()
        rooms=[i for i in range(n)]
        end_time=[]
        di=defaultdict(int)
        for s,e in meetings:
            while end_time and end_time[0][0]<=s:
                end,r=heappop(end_time)
                heappush(rooms,r)
            if rooms:
                used_room=heappop(rooms)   
            else:
                end,room=heappop(end_time)
                duration=e-s
                s=end
                e=(s+duration)
                used_room=room
            di[used_room]+=1
            heappush(end_time,(e,used_room))
        max_value=max(di.values())
        for i,j in di.items():
            if j==max_value:
                return i