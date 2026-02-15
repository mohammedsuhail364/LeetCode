class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=defaultdict(int)
        l=0
        res=0
        for r in range(len(s)):
            count[s[r]]+=1
            if (r-l+1)>3:
                count[s[l]]-=1
                if count[s[l]]==0:
                    del count[s[l]]
                l+=1
            if (r-l+1)==3 and len(count)==3:
                res+=1
        return res

