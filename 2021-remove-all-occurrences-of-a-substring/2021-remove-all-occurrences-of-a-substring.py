class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part=list(part)
        p_len=len(part)
        stack=[]
        for c in s:
            stack.append(c)
            if len(stack)>=p_len and stack[-p_len:]==part:
                count=p_len
                while count:
                    stack.pop()
                    count-=1
        return ''.join(stack)