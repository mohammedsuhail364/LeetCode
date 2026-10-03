class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1] # because it consider this as a close bracket at start
        res=0
        for idx,i in enumerate(s):
            if i=="(":
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    res=max(res,idx-stack[-1])
        return res