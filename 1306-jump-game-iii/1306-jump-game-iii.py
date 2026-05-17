class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visit={}
        def dfs(i):
            if i>=len(arr) or i<0:
                return False
            if i in visit:
                return visit[i]
            if arr[i]==0:
                return True
            visit[i]=False
            visit[i] = dfs(i+arr[i]) or dfs(i-arr[i])
            return visit[i]
        return dfs(start)