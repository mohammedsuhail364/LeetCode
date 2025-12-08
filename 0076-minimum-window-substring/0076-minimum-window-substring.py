class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq=Counter(t)
        s_freq=defaultdict(int)
        have=0
        need=len(t_freq)
        l=0
        res=""
        min_len=inf
        for r in range(len(s)):
            s_freq[s[r]]+=1
            if t_freq[s[r]]== s_freq[s[r]]:
                have+=1
            while need==have:
                if (r-l+1)<min_len:
                    min_len=(r-l+1)
                    res=s[l:r+1]
                s_freq[s[l]]-=1
                if s[l] in t_freq and t_freq[s[l]]>s_freq[s[l]]:
                    have-=1
                l+=1
            
        return res
            
            
