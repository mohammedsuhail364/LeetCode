class Solution:
    def countCommas(self, n: int) -> int:
        # refer this https://leetcode.com/problems/count-commas-in-range-ii/solutions/8510746/comma-pattern-range-counting-simple-math-uptf
        res=0
        threshold  = 1000
        while threshold<=n:
            res+=(n-threshold+1) # that means if the n=1003 then 1003 - 1000 + 1(999) which after 999 all numbers contain at least one comma after we increase the threshold by multiple 1000
            threshold*=1000 # next comma happen,if n less than or equal to threshold then it definetely contains another comma
        return res