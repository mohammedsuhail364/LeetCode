class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(i):
            if i>n:
                return 0
            if i==n:
                return 1
            return helper(i+1)+helper(i+2)
        return helper(0)
            