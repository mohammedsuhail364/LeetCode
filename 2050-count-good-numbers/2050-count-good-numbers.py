class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def find_power_val(x,n):
            res=1
            x=x%mod
            while n>0:
                if n%2:
                    res=(res*x)%mod
                x=(x*x)%mod
                n=n//2
            return res%mod

        mod = 10**9 + 7
        even_position = (n+1)//2
        odd_position = n//2
        return ((find_power_val(5,even_position)*find_power_val(4,odd_position))%mod)
        