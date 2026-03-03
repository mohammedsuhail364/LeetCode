class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            temp=''
            for i in s:
                if i=='1':
                    temp+='0'
                else:
                    temp+='1'
            return temp
        s='0'
        while n:
            s=s+'1'+invert(s)[::-1]
            n-=1
        return s[k-1]

            