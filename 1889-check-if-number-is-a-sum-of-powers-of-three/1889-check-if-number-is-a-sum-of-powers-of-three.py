class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(power,n):
            if n==0:
                return True
            if 3**power>n:
                return False
            add_power=backtrack(power+1,n-3**power)
            skip_power=backtrack(power+1,n)
            return add_power or skip_power
        return backtrack(0,n)