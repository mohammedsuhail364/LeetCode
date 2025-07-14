class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        def helper(word):
            stack=[]
            for i in word:
                if i=='#' and stack:
                    stack.pop()
                else:
                    stack.append(i)
            res=''
            for i in stack:
                if i=='#':
                    continue
                res+=i
            return res
        return helper(s)==helper(t)
        