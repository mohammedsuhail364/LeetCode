class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        res=''
        for i in s:
            if i !=']':
                stack.append(i)
            else:
                string=''
                number=''
                while stack:
                    val=stack.pop()
                    if val=='[':
                        break
                    
                    string = val + string
                while stack:
                    val=stack.pop()
                    if not (val in '1234567890'):
                        stack.append(val)
                        break
                    number+=val
                number=int(number[::-1])
                tmp=string*number
                stack.append(tmp)
        return ''.join(stack)    