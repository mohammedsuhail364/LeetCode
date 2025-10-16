class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        # refer neetcode
        def dfs(count,paste):
            if count==n:
                return 0
            if count>n:
                return float('inf')
            copy_and_paste=2+dfs(count+count,count)
            paste=1+dfs(count+paste,paste)
            return min(copy_and_paste,paste)
        return 1+dfs(1,1)