class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        if int(s,2)<=k:
            return len(s)
        val=int(s,2)
        res=len(s)
        power=len(s)-1
        for i in range(len(s)):
            if s[i]=='1':
                val-=2**power
                res-=1
            
            if val<=k:
                return res
            power-=1
        
            