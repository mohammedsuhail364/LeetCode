class Solution:
    def maximumEnergy(self, energy, k: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i):
            if i >= len(energy):
                return 0
            return energy[i] + dfs(i + k)

        return max(dfs(i) for i in range(len(energy)))
