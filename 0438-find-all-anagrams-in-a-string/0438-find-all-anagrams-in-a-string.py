class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count=Counter(p)
        s_count=defaultdict(int)
        l=0
        
        res=[]
        for r in range(len(s)):
            s_count[s[r]]+=1
            if (r-l+1)>len(p):
                s_count[s[l]]-=1
                if s_count[s[l]]==0:
                    del s_count[s[l]]
                l+=1
            if p_count==s_count:
                res.append(l)
        return res