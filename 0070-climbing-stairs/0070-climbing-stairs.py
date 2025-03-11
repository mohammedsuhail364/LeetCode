class Solution:
    def climbStairs(self, n: int) -> int:
        cache={}
        def backtrack(cur_sum):
            if cur_sum==n:
                return 1
            if cur_sum>n:
                return 0
            if cur_sum in cache:
                return cache[cur_sum]
            ways=0
            for x in [1,2]:
                ways+=backtrack(cur_sum+x)
            cache[cur_sum]=ways
            return ways
        return backtrack(0)