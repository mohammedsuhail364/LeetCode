class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num2=0
        for i in range(m,n+1,m):
            num2+=i
        range_sum=(n*(n+1))//2
        num1=range_sum-num2
        return num1-num2