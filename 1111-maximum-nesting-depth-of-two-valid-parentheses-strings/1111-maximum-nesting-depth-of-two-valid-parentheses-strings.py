class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        openCount=0
        res=[]
        for i in seq:
            if i==")":
                openCount-=1
                res.append(openCount%2)
            elif i=="(":
                res.append(openCount%2)
                openCount+=1
        return res