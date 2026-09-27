class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            if i==")":
                t=""
                while stack and stack[-1]!='(':
                    t+=stack.pop()
                if stack and stack[-1]=="(":
                    stack.pop()
                for x in t:
                    stack.append(x)
            else:
                stack.append(i)
        return ''.join(stack)
        