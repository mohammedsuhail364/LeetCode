class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # this is a stack based problem 
        # why because if we see the greater element in the stack we can remove that
        stack=[]
        for n in num:
            while stack and k>0 and stack[-1]>n:
                stack.pop()
                k-=1
            stack.append(n)
        # if k is there
        while k>0:
            stack.pop()
            k-=1
        res=''.join(stack).lstrip('0')
        return res if res else "0"