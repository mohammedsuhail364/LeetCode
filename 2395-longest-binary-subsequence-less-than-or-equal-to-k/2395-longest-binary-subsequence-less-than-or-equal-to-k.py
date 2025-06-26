class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        if int(s,2)<=k:
            return len(s)
        s=list(s)
        res=len(s)
        for i in range(len(s)):
            if s[i]=='1':
                s[i]='0'
                res-=1
            val=''.join(s)
            if int(val,2)<=k:
                return res
        
            