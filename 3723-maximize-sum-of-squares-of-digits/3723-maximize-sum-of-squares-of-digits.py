class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>9*num: # which is maximum we get
            return ""
        digit = []
        for i in range(num):
            val = min(9,sum)
            digit.append(str(val))
            sum-=val
        if sum>0:
            return ""
        return "".join(digit)