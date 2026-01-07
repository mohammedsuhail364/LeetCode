class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count=0
        res=''
        for i in s:
            if i=='(':
                count+=1
                if count>1:
                    res+=i
            else:
                count-=1
                if count>0:
                    res+=i
        return res