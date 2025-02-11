class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        i=0
        j=len(part)
        while j<=len(s):
            k=s[i:j]
            if s[i:j]==part:
                s=s[:i]+s[j:]
                i=0
                j=len(part)
            else:
                i+=1
                j+=1
        return s