class Solution:
    def coloredCells(self, n: int) -> int:
        """
        the pattern is n=1 -> 1
        n -> 2    1+3+1
        n -> 3    1+3+5+3+1
        n -> 4    1+3+5+7+5+3+1
        """
        cur_sum=0
        odd_val=1
        for i in range(n):
            cur_sum+=odd_val
            odd_val+=2
        odd_val-=4
        for i in range(n-1):
            cur_sum+=odd_val
            odd_val-=2
        return cur_sum

