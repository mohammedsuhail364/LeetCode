class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:

        if sum>9*num: # which is maximum we get
            return ""
        q,r = divmod(sum,9)
        res = "9"*q
        if r>0:
            res+=str(r)
        s = "0"*(num-len(res))
        return res+s