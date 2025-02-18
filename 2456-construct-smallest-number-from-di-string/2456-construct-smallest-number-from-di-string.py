class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n=len(pattern)
        used=[False]*(n+1)
        num_arr=[]
        def backtrack(idx):
            if idx>=n:
                return True
            nonlocal num_arr
            start= 0 if idx==-1 or pattern[idx]=='D' else num_arr[-1]
            end= n+1 if idx==-1 or pattern[idx]=='I' else num_arr[-1]
            for i in range(start,end):
                if used[i]:
                    continue
                used[i]=True
                num_arr.append(i+1)
                if backtrack(idx+1):
                    return True
                num_arr.pop()
                used[i]=False
        
        backtrack(-1)
        
        return ''.join([str(num) for num in num_arr])