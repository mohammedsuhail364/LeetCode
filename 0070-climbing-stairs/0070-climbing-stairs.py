class Solution:
    def climbStairs(self, n: int) -> int:
        # fibanocci number
        first=0
        second=1
        for i in range(n):
            third=first+second
            first=second
            second=third
        return third
