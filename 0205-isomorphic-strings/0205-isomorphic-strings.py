class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t={}
        t_to_s={}
        for i,j in zip(s,t):
            if i not in s_to_t:
                s_to_t[i]=j
            else:
                if not s_to_t[i]==j:
                    return False
            if j not in t_to_s:
                if j not in t_to_s:
                    t_to_s[j]=i
            else:
                if not t_to_s[j]==i:
                    return False
        return True
            