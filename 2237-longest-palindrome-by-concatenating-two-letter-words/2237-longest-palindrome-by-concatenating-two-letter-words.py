class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        visited=set()
        count=Counter(words)
        res=0
        flag=True
        for s,cnt in count.items():
            if s in visited:
                continue
            if s[0]==s[1]:
                if cnt%2:
                    cnt-=1
                    if flag:
                        res+=2
                        flag=False
                res+=(cnt*2)
                continue
            ss=s[1]+s[0]
            max_add=min(cnt,count[ss])
            res+=(max_add*2)*2
            visited.add(s)
            visited.add(ss)
        return res