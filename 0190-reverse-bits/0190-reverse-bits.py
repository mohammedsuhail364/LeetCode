class Solution:
    def reverseBits(self, n: int) -> int:
        val=bin(n)[2:][::-1]
        c='0'*(32-len(val))
        return int(val+c,2)
        
            