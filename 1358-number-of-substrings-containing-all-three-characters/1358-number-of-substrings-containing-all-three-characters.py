class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        count=defaultdict(int)
        res=0
        for r in range(len(s)):
            count[s[r]]+=1
            while len(count)==3:
                res+=(len(s)-r)
                count[s[l]]-=1
                if count[s[l]]==0:
                    del count[s[l]]
                # (len(s)-r) -> this is the key for this question why it exists if the (l-r) is good then (l-len(s)) also good because it defintely contains atleast of (a,b,c)
                # so we count len(s)-r give the valid good substrings
                l+=1

        return res