class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            
            if i not in '*/+-':
                stack.append(i)
            else:
                second=stack.pop()
                first=stack.pop()
                res=first+i+second
                k=str(int(eval(res)))
                stack.append(k)
        ans=stack[-1]
        return int(ans)