class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        di=set()
        res=0
        for r in range(len(s)):  
            while s[r] in di:
                di.remove(s[l])
                l+=1
            di.add(s[r])
            res=max(res,r-l+1)
        return res