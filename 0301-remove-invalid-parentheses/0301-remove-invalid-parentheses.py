class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            count=0
            for i in s:
                if i=='(':
                    count+=1
                elif i==')':
                    count-=1
                    if count<0:
                        return False
            return count==0

        q=deque([s])
        visited=set([s])
        res=[]
        found=False
        while q:
            size=len(q)
            for _ in range(size):
                cur=q.popleft()
                if is_valid(cur):
                    res.append(cur)
                    found=True
                    continue   
                for i in range(len(cur)):
                    if cur[i] not in '()':
                        continue
                    next_str=cur[:i]+cur[i+1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        q.append(next_str)
            if found:
                break # because we get the minimal removal one (level wise)
        return res

             
            
            