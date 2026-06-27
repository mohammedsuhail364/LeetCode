class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        _s1 = [0]*26
        _s2 = [0]*26
        for i in s1:
            idx=ord(i)-ord('a')
            _s1[idx]+=1
        l=0
        for r in range(len(s2)):
            
            if (r-l+1)>len(s1):
                idx=ord(s2[l])-ord('a')
                l+=1
                _s2[idx]-=1
            idx=ord(s2[r])-ord('a')
            _s2[idx]+=1
            if (r-l+1)==len(s1) and _s1==_s2:
                return True
        return False