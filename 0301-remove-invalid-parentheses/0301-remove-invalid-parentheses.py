class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # this question normally intuates the dfs solution but doing dfs is not a great thing 
        # why because if we find the level of which is the minimum removal means we dont try other higher levels 
        # so it automatically drives into bfs solution basically try every possibilities but with level by level
        def is_valid(val):
            brackets = 0
            for i in val:
                if i=="(":brackets+=1
                elif i==")":
                    brackets-=1
                    if brackets<0:return False
            return brackets==0
        q=deque([(s)])
        visited=set()
        res=[]
        found = False
        while q:
            
            n=len(q)
            for _ in range(n):
                val = q.popleft()
                if is_valid(val):
                    res.append(val)
                    found = True
                    continue
                for i in range(len(val)): # try all possibities without involving letters
                    if val[i] not in "()":
                        continue
                    next_str=val[:i]+val[i+1:]
                    if next_str not in visited:
                        q.append(next_str)
                        visited.add(next_str)

            if found:
                break # this logic differs the bfs sol is better than dfs we break after reach the minimum level after this we cannot because already we remove some thing after this we remove some other thing so that is not a minimum level
        return res
