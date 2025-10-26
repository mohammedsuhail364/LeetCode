class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>9*num:
            return ""
        digits=[]
        for i in range(num):
            val=min(9,sum)
            digits.append(str(val))
            sum-=val
        if sum>0:
            return ""
        return "".join(digits)