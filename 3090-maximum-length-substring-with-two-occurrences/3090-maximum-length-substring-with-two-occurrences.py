class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l=0
        res=0
        c=defaultdict(int)
        for r in range(len(s)):
            c[s[r]]+=1
            while c[s[r]]>2:
                c[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res