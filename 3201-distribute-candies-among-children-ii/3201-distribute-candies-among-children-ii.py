class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res=0
        for i in range(min(n,limit)+1):
            rem=n-i
            if rem>2*limit:continue
            min_val=max(rem-limit,0)
            max_val=min(rem,limit)
            res+=(max_val-min_val+1)
        return res