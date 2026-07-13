class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        q=deque(range(1,10))
        res=[]
        while q:
            t=q.popleft()
            if t<=high:
                if t>=low:
                    res.append(t)
                last=t%10
                if last<9:
                    nxt=t*10+last+1
                    if nxt <= high:
                        q.append(nxt)
        return res
