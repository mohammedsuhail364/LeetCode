class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n=len(s)
        tmp=""
        if n%k!=0:
            v=n%k
            tmp=fill*(k-v)
        i=0
        j=k
        res=[]
        while i<n:
            temp=s[i:j]
            res.append(temp)
            i+=k
            j+=k
        
        if n:
            res.append(res.pop()+tmp)
        return res