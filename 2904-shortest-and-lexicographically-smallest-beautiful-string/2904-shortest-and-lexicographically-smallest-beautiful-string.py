class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res="1"*(len(s)+1)
        for i in range(len(s)):
            oneCount=0
            for j in range(i,len(s)):
                t=s[i:j+1]
                if s[j]=="1":
                    oneCount+=1
                if oneCount==k:
                    if len(res)>j-i+1:
                        res=t
                    elif len(res)==j-i+1:
                        res=min(res,t)
                elif oneCount>k:
                    break
        return res if res!="1"*(len(s)+1) else ""