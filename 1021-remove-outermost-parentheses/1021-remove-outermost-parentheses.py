class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        f=0
        b=0
        res=[]
        for i in s:
            if i=='(':
                stack.append(i)
                f+=1
            else:
                stack.append(i)
                b+=1
                if f==b:
                    tmp=''.join(stack[1:-1]) 
                    res.append(tmp)
                    stack=[]
        return ''.join(res)