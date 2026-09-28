class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        res=0
        for i in s:
            if i==")":
                if stack and stack[-1]=="(":
                    res=max(res,len(stack))
                    stack.pop()
            elif i=="(":
                stack.append(i)
        return res