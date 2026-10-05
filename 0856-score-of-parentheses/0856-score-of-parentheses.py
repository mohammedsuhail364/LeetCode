class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0] # the first value ensure this is no level now
        for i in s:
            if i=="(":
                stack.append(0)
            else:
                top = stack.pop()
                stack[-1]+=max(2*top,1)
        return stack[0]