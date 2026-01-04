class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        di={')':"(","}":'{',']':'['} # key is closing brackets and value is opening brackets
        for c in s:
            # if we see opening brackets we can add on the stack
            if c in di.values():
                stack.append(c)
            # if we see the closing brackets we can check in the stack there is open brackets for this
            elif c in di:
                if not stack or stack.pop()!=di[c]:
                    return False
        return not stack
        