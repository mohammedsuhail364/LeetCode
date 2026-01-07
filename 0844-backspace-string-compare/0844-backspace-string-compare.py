class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def find(word):
            stack=[]
            for i in word:
                if i!='#':
                    stack.append(i)
                else:
                    if stack:
                        stack.pop()
            return ''.join(stack)
        s=find(s)
        t=find(t)
        return s==t