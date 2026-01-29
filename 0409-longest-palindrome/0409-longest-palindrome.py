class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq=Counter(s)
        c=0
        res=0
        odd=False
        for i,j in freq.items():
            if j%2==0:
                res+=j
            else:
                res+=(j-1) # add all the even ones and indicate there is one additional we have
                odd=True
            
        return res+1 if odd else res