class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # a+b=n
        # a=n-b
        def check(val):
            while val:
                tmp=val%10
                if tmp==0:
                    return False
                val//=10
            return True
        for b in range(1,n): 
            a=n-b
            if check(a) and check(b):
                return [a,b]
