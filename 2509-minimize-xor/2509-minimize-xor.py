class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        a=list(bin(num1)[2:])
        num1_bin=bin(num1).count('1')
        num2_bin=bin(num2).count('1')
        if num1_bin>num2_bin:
            y=len(a)-1
            for _ in range(num1_bin-num2_bin):
                while y>=0 and a[y]!='1':
                    y-=1
                if y>=0:
                    a[y]='0'
                    y-=1
        elif num1_bin<num2_bin:
            y=len(a)-1
            for _ in range(num2_bin-num1_bin):
                while y>=0 and a[y]!='0':
                    y-=1
                if y>=0:
                    a[y]='1'
                else:
                    a.insert(0,'1')
                y-=1
        return int(''.join(a),2)