class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        _p=[0]*26
        _s=[0]*26
        for i in p:
            idx=ord(i)-ord('a')
            _p[idx]+=1
        l=0
        res=[]
        for r in range(len(s)):
            if (r-l+1)>len(p):
                idx=ord(s[l])-ord('a')
                _s[idx]-=1
                l+=1
            idx=ord(s[r])-ord('a')
            _s[idx]+=1
            if (r-l+1)==len(p) and _p==_s:
                res.append(l)
        return res