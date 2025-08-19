class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i=0
        j=i+1
        while j<len(bits):
            if bits[i]==0:
                i+=1
                j+=1
                continue
            bits[i]=-1
            bits[j]=-1
            i=j+1
            j=i+1
        return bits[-1]==0