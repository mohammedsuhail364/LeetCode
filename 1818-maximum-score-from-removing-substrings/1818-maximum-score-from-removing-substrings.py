class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack=[]
        want_to_remove=''
        max_val=0
        min_val=0
        res=0
        
        if x>y:
            want_to_remove='ab'
            max_val=x
            min_val=y
        else:
            want_to_remove='ba'
            max_val=y
            min_val=x
        for i in range(len(s)):
            if stack and stack[-1]+s[i]==want_to_remove:
                res+=max_val
                stack.pop()
            else:
                stack.append(s[i])
        want_to_remove='ba' if want_to_remove=='ab' else 'ab'
        s=''.join(stack)
        stack=[]
        for i in range(len(s)):
            if stack and stack[-1]+s[i]==want_to_remove:
                res+=min_val
                stack.pop()
            else:
                stack.append(s[i])
        return res