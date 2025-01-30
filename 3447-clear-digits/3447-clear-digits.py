class Solution:
    def clearDigits(self, s: str) -> str:
        li=[]
        for i in s:
            if i in '1234567890' and li:
                li.pop()
            else:
                li.append(i)
        return ''.join(li)