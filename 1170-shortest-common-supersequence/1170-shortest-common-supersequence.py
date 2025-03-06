class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n,m=len(str1),len(str2)
        prev=[str2[j:] for j in range(m)]
        prev.append('')
        for i in reversed(range(n)):
            cur=['']*m
            cur.append(str1[i:])
            for j in reversed(range(m)):
                if str1[i]==str2[j]:
                    cur[j]=str1[i]+prev[j+1]
                else:
                    res1=str1[i]+prev[j]
                    res2=str2[j]+cur[j+1]
                    if len(res1)<len(res2):
                        cur[j]=res1
                    else:
                        cur[j]=res2
            prev=cur
        return cur[0]