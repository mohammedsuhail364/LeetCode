class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            c=s[i]
            val=26-(ord(c)-ord('a'))
            res+=(val*(i+1))
        return res