class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        seen=defaultdict(int)
        for r in range(len(s)):
            seen[s[r]]+=1
            while seen[s[r]]>1:
                seen[s[l]]-=1
                l+=1
            res=max(res,(r-l+1))
        return res