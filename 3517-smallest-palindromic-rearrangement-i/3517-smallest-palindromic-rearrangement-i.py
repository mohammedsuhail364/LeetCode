class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count=Counter(s)
        print(count)
        oddchar=""
        res=[]
        for w,c in count.items():
            if c%2!=0:
                oddchar+=w
            res.append((w*(c//2)) if c!=1 else "")
        res.sort()
        res=''.join(res)
        res=res+oddchar+res[::-1]
        return res