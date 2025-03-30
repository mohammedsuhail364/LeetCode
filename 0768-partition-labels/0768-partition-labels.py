class Solution:
    def partitionLabels(self, s: str):
        di={s1:i for i,s1 in enumerate(s)}   
        # print(di)
        i=0
        res=[]
        while i<len(s):
            
            last=di[s[i]]
            x=i
            while x<len(s) and x<=last:
                if di[s[x]]>last:
                    last=di[s[x]]
                x+=1
            res.append(last-i+1)
            i=x
        return res