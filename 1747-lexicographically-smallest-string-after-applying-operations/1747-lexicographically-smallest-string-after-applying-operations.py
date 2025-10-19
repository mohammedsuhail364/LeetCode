class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        res=s
        visit=set([(s)])
        q=deque([(s)])
        while q:
            cur=q.popleft()
            if cur<res:
                res=cur
            temp=list(cur)
            for i in range(1,len(temp),2):
                temp[i]=str((int(temp[i])+a)%10)
            added=''.join(temp)
            if added not in visit:
                q.append(added)
                visit.add(added)
            rotate=cur[-b:]+cur[:-b]
            if rotate not in visit:
                q.append(rotate)
                visit.add(rotate)
        return res
