class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(power,cur_sum):
            if cur_sum==n:
                return True
            if 3**power>n:
                return False
            add_power=backtrack(power+1,cur_sum+3**power)
            skip_power=backtrack(power+1,cur_sum)
            return add_power or skip_power
        return backtrack(0,0)