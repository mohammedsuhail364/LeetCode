class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return (s[l+1:r+1]==s[l+1:r+1][::-1] or s[l:r]==s[l:r][::-1])
            l+=1
            r-=1
        return True
