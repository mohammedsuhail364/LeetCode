class Solution:
    def reverseBits(self, n: int) -> int:
        tmp=['0']*32
        val=bin(n)[2:]
        x=0
        for i in reversed(range(len(val))):
            tmp[x]=val[i]
            x+=1
        return int(''.join(tmp),2)