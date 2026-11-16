class Solution:
    def digitSum(self, s: str, k: int) -> str:
        s=list(s)
        while len(s)>k:
            sp=[]
            cur=0
            for x in range(len(s)):
                cur+=int(s[x])
                if (x+1)%k==0:
                    sp.append(str(cur))
                    cur=0
            if (x+1)%k:sp.append(str(cur))
            s=list(''.join(sp))
        return ''.join(s)