class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        res=0
        open_count=0
        for i in s:
            if i !=")":
                stack.append(i)
                open_count+=1 if i=="(" else 0
                res=max(res,open_count)
            elif i==")":
                while stack and stack[-1]!="(":
                    stack.pop()
                open_count-=1
                stack.pop()
        return res