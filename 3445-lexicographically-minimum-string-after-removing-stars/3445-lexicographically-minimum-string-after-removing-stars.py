class Solution:
    def clearStars(self, s: str) -> str:
        s=list(s)
        freq={chr(i):[] for i in range(97,97+26)}
        for i in range(len(s)):
            if s[i]!='*':
                freq[s[i]].append(i)
            else:
                for x,y in freq.items():
                    if y:
                        pos=y.pop()
                        break
                s[pos]='*'
        res=''
        for i in s:
            res+= i if i !='*' else ''
        return res