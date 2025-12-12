class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_freq=Counter(p)
        s_freq=defaultdict(int)
        l=0
        res=[]
        for r in range(len(s)):
            s_freq[s[r]]+=1
            if (r-l+1)>len(p):
                s_freq[s[l]]-=1
                if s_freq[s[l]]==0:
                    del s_freq[s[l]]
                l+=1
            if p_freq==s_freq:
                res.append(l)
        return res