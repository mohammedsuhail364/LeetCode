class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened=0
        res=0
        for i in s:
            if i=="(":opened+=1
            else:
                if opened:
                    opened-=1
                else:
                    res+=1
        return res+opened