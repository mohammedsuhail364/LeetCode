class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i=0
        index=set()
        
        while i<len(s) and s[i]=='1':
            i+=1
        for x in range(i,len(s)):
            if s[x]=='1':
                return False
        return True