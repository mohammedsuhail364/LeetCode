class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_freq=defaultdict(int)
        t_freq=Counter(t)
        n=len(t_freq)
        l=0
        matches=0
        res=''
        min_len=inf
        for r in range(len(s)):
            s_freq[s[r]]+=1
            if s_freq[s[r]]==t_freq[s[r]]:
                matches+=1
            while matches==n:
                if (r-l+1)<min_len:
                    res=s[l:r+1]
                    min_len=r-l+1
                s_freq[s[l]]-=1
                if s_freq[s[l]]<t_freq[s[l]]:
                    matches-=1
                l+=1
        return res
            