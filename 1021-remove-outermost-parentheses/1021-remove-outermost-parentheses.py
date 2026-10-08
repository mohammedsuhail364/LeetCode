class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # this question is basically asks as need to remove the outer most parenthesis 
        # so we can run a loop if it starts means we dont add in the res
        res=[]
        c=0
        for i in s:
            if i=="(":
                c+=1
                if c>1:res.append(i)
            else:
                c-=1
                if c>0:res.append(i)
        return ''.join(res)