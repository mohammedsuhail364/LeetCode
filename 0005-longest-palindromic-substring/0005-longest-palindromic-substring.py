class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        def expand(r,l):
            while 0<=l<len(s) and 0<=r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            # when loop breaks, l and r are ONE step outside
            # so valid palindrome is s[l+1 : r]
            return s[l+1:r]
        for i in range(len(s)):
            odd=expand(i,i)
            even=expand(i,i+1)
            if len(odd)>len(res): res=odd
            if len(even)>len(res): res=even

        return res