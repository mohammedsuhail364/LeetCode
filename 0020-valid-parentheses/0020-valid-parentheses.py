class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets={'(':')','{':'}','[':']'}
        for i in s:
            if i in brackets:
                stack.append(brackets[i])
            else:
                if stack==[] or stack.pop()!=i:
                    return False
        return len(stack)==0