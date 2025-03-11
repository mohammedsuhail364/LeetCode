class Solution:
    def climbStairs(self, n: int) -> int:
        i,j=0,1
        for x in range(n):
            third=i+j
            i=j
            j=third
        return third
        