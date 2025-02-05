class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        s1=list(s1)
        s2=list(s2)
        for i in range(len(s1)):
            for j in range(i+1,len(s1)):
                s1[i],s1[j]=s1[j],s1[i]
                if s1==s2:
                    return True
                s1[i],s1[j]=s1[j],s1[i]
        return False