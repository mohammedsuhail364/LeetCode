class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        l,r=0,len(s)-1
        while l<r:
            while l<len(s) and s[l] not in 'aeiouAEIOU':
                l+=1
            while r>0 and s[r] not in 'aeiouAEIOU':
                r-=1
            if l<r:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
        return ''.join(s)
        