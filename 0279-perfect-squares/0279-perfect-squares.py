class Solution:
    def numSquares(self, n: int) -> int:
        squares=[i*i for i in range(int(sqrt(n))+1)]
        q=deque([(0,0)])
        visit=set([0])
        while q:
            total,steps=q.popleft()
            for x in squares:
                nxt=total+x
                if nxt==n:
                    return steps+1
                if nxt<n and nxt not in visit:
                    visit.add(nxt)
                    q.append((nxt,steps+1))
        