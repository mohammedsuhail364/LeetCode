class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_count=Counter()
        t_count=Counter(t)
        l=0
        res=''
        have=0
        min_len=float('inf')
        need=len(t_count)
        for r in range(len(s)):
            s_count[s[r]]+=1
            if s_count[s[r]]==t_count[s[r]]:
                have+=1
            while need==have:
                if (r-l+1)<min_len:
                    res=s[l:r+1]
                    min_len=r-l+1
                s_count[s[l]]-=1
                if s[l] in t_count and s_count[s[l]]<t_count[s[l]]:
                    have-=1
                l+=1
        return res
