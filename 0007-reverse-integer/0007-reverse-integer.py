class Solution:
    def reverse(self, x: int) -> int:
        x1=str(x)
        if x1[0]=='-':
            x=x1.replace('-','')
            a='-' + x[::-1]
            return int(a) if -2**31 <= int(a) <= 2**31 - 1 else 0
        else:
            a=x1[::-1]
            return int(a) if -2**31 <= int (a) <= 2**31 -1 else 0

        