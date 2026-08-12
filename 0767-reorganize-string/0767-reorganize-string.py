class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        x=max(count.values())
        n=len(s)
        if x>(n+1)//2:return ""
        max_heap=[(v,k) for k,v in count.items()]

        heapify_max(max_heap)
        res=''
        q=deque()
        while max_heap or q:
            if max_heap:
                c,w=heappop_max(max_heap)
                res+=w
                c-=1
                if c>0:
                    q.append((c,w))
            if q and res:
                c,w=q[0][0],q[0][1]
                if c>0 and w!=res[-1]:
                    heappush_max(max_heap,q.popleft())
        return res