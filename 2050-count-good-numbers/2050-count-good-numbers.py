class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_position = (n+1)//2
        odd_position = n//2
        return ((pow(5,even_position,MOD)*pow(4,odd_position,MOD))%MOD)
        