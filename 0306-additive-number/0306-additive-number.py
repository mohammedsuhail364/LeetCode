class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n=len(num)
        def is_valid(a,b,remain):
            while remain:
                c=str(int(a)+int(b))
                if not remain.startswith(c):
                    return False
                remain=remain[len(c):]
                a,b=b,c
            return True
        for i in range(1,n):
            for j in range(i+1,n):
                a=num[:i]
                b=num[i:j]
                remain=num[j:]
                if ((len(a)>1 and a[0]=='0') or (len(b)>1 and b[0]=='0')):
                    continue
                if is_valid(a,b,remain):
                    return True
        return False