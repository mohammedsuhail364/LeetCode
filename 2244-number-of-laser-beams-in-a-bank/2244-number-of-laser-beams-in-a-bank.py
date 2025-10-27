class Solution:
    def numberOfBeams(self, bank) -> int:
        n=len(bank)
        prev=0
        cur=1
        res=0
        while cur<n:
            while prev<n and bank[prev].count('1')==0:
                prev+=1
            if cur==prev:
                cur+=1
            while cur<n and bank[cur].count('1')==0:
                cur+=1
            if cur<n and prev<n:
                res+=(bank[prev].count('1')*bank[cur].count('1'))
            prev+=1
            cur+=1
        return res