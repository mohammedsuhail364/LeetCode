class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        r=len(s)-1
        s=list(s)
        while l<r:
            while l<r and s[l] not in "aeiouAEIOU":
                l+=1
            while l<r and s[r] not in "aeiouAEIOU":
                r-=1
            if l!=r:
                s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return ''.join(s)