# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l=0
        r=n
        while l<=r:
            pick=(l+r)//2
            val=guess(pick)
            if val==0:
                return pick
            if val<0:
                r=pick-1
            else:
                l=pick+1
        