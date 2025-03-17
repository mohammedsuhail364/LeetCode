class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            
            if i not in '*/+-':
                stack.append(i)
            else:
                second=int(stack.pop())
                first=int(stack.pop())
                if i=='+':
                    k=first+second
                elif i=='-':
                    k=first-second
                elif i=='*':
                    k=first*second
                elif i=='/':
                    k=first/second
                stack.append(k)
        ans=stack[-1]
        return int(ans)