class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        self.res=0
        events.sort()
        n=len(events)
        memo={}
        def find_index(i):
            for j in range(i+1,n):
                if events[i][1]<+ events[j][0]:
                    return j
            return n
        def backtrack(i,step):
            if i==n or step==k:
                return 0
            if (i,step) in memo:
                return memo[(i,step)]
            # skip the current
            skip=backtrack(i+1,step)
            # include the current
            next_idx=find_index(i)
            include = events[i][2]+backtrack(next_idx,step+1)
            memo[(i,step)]=max(skip,include)
            return memo[(i,step)]
        return backtrack(0,0)
        