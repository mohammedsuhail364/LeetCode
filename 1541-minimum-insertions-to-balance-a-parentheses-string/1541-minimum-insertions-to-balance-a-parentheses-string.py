class Solution:
    def minInsertions(self, s: str) -> int:
        # refer this https://www.youtube.com/watch?v=YNGteCvRunY
        need = 0
        res = 0
        for i in s:
            if i=="(":
                if need%2:
                    need-=1
                    res+=1
                need+=2
            else:
                need-=1
                if need<0:
                    res+=1
                    need=1
        return res+need