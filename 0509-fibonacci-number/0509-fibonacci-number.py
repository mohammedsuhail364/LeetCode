class Solution:
    def fib(self, n: int) -> int:
        if n==1 or n==0:
            return n
        first=0
        second=1
        third=0
        for i in range(n-1):
            third=first+second
            first=second
            second=third
        return third
        # 0 1 1 2


