class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        val=bin(n)[2:]
        for i in range(1,len(val)):
            if val[i]==val[i-1]:
                return False
        return True