class Solution:
    def minimumLength(self, s: str) -> int:
        s=list(s)
        i=1
        while i<len(s):
            j=i-1
            k=i+1
            if s[i]=='':
                i+=1
                continue
            while j>-1 and s[j]!=s[i]:
                j-=1
            if j==-1:
                i+=1
                continue
            
            while k<len(s) and s[k]!=s[i]:
                k+=1
            if k==len(s):
                i+=1
                continue
            if s[j]==s[k]:
                s[j]=''
                s[k]=''
            i+=1
        c=0
        for i in s:
            if i != '':
                c+=1
        return c