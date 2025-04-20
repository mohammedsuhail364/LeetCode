class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a=int(dividend/divisor)
        if a==2**31:
            return a-1
        return a