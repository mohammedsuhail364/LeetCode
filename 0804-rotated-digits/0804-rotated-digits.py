class Solution:
    def rotatedDigits(self, n: int) -> int:
        res=0
        invalid={'3','7','4'}
        different={'2','5','6','9'}
        res=0
        for i in range(1,n+1):
            tmp=str(i)
            if any(ch in invalid for ch in tmp):
                continue
            if any(ch in different for ch in tmp):
                res+=1
        return res
