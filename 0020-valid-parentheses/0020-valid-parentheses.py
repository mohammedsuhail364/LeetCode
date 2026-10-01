class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets = {")":"(","}":"{","]":"["}
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                k=brackets[i]
                if not stack:return False
                if stack[-1]!=k:return False
                stack.pop()
        return not stack