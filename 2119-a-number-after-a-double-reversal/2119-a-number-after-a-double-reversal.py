class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        rev = int(str(num)[::-1])
        return int(str(rev)[::-1])==num