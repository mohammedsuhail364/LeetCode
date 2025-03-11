from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        res=0
        count=[0]*3
        for r in range(len(s)):
            count[ord(s[r])-ord('a')]+=1
            while count[0] and count[1] and count[2] :
                res+=len(s)-r
                count[ord(s[l])- ord('a')]-=1
                l+=1
        return res