class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix=[0]*(len(s)+1)
        for st,e,d in shifts:
            prefix[e+1]+=1 if d==1 else -1
            prefix[st]+=-1 if d==1 else 1
        res=[ord(c)-ord('a') for c in s]
        diff=0
        for i in reversed(range(len(prefix))):
            diff+=prefix[i]
            res[i-1]=(diff+res[i-1]+26)%26
        s=[ chr(ord('a')+n) for n in res ]
        return ''.join(s)