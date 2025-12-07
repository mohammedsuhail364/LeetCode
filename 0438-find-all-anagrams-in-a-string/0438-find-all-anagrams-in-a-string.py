class Solution:
    def findAnagrams(self, s: str, p: str):
        def convert_to_index(i):
            return ord(i)-ord('a')
        p_count=[0]*26
        s_count=[0]*26
        for i in p:
            index=convert_to_index(i)
            p_count[index]+=1
        l=0
        res=[]
        for r in range(len(s)):
            index=convert_to_index(s[r])
            s_count[index]+=1
            if (r-l+1)>len(p):
                index=convert_to_index(s[l])
                s_count[index]-=1
                l+=1
            if s_count==p_count:
                res.append(l)
        return res
