class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            temp=['0' if i=='1' else '1' for i in s]
            return ''.join(temp)
        s='0'
        while n:
            s=s+'1'+invert(s)[::-1]
            if k<=len(s):
                s[k-1]
            n-=1
        return s[k-1]

            