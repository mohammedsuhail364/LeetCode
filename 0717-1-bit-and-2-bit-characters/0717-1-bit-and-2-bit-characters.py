class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i=0
        isValid=False
        while i<len(bits):
            if bits[i]==1:
                if i+1<len(bits):
                    i+=1
                isValid=False
            else:
                isValid=True
            i+=1
        return isValid

                