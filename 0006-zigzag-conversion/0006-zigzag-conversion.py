class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        # refer neetcode 
        res=""
        for r in range(numRows):
            increment=2*(numRows-1)
            for i in range(r,len(s),increment):
                res+=s[i]
                if r in [0,numRows-1]:
                    continue
                if (i+increment-2*r < len(s)):
                    res+=s[i+increment-2*r ]
        return res