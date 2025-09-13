class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i!=']':
                stack.append(i)
            else:
                subString=''
                while stack and stack[-1]!='[':
                    subString=stack.pop()+subString
                stack.pop()
                count=''
                while stack and stack[-1].isdigit():
                    count=stack.pop()+count
                
                stack.append(int(count)*subString)
        return ''.join(stack)
