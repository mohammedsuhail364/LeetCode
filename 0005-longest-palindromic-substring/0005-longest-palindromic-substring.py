class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=''
        res_len=0
        for i in range(len(s)):
            # check odd length
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>res_len:
                    res_len=(r-l+1)
                    res=s[l:r+1]
                l-=1
                r+=1
            # check even length
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>res_len:
                    res_len=(r-l+1)
                    res=s[l:r+1]
                l-=1
                r+=1
        return res