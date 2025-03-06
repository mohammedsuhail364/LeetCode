class Solution:
    def shortestPalindrome(self, s: str) -> str:
        l=0
        r=len(s)
        while l<=r:
            k=s[l:r]
            if k==k[::-1]:
                j=s[r:][::-1]
                return j+s
            else:
                r-=1
