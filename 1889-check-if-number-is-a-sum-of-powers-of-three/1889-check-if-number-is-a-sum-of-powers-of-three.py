class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            val=n%3
            if val==2:
                return False
            n=n//3
        return True