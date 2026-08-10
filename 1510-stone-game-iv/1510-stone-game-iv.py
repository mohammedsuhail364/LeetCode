class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dfs(n):
            sq=1
            while sq*sq<=n:
                if not dfs(n-sq*sq):
                    return True
                sq+=1
            return False
        return dfs(n)