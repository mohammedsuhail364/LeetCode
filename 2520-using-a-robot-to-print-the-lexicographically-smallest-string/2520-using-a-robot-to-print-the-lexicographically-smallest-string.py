class Solution:
    def robotWithString(self, s: str) -> str:
        def check_smallest_string():
            for i in range(26):
                if freq[i]:
                    return 97+i # (97 for ord('a'))
            return 97+25 # (97 for ord('a'))
        freq=[0]*26
        for i in s:
            freq[ord(i)-ord('a')]+=1
        t=[] # stack
        pos=0
        res=''
        while pos<len(s):
            t.append(s[pos])
            freq[ord(s[pos])-ord('a')]-=1

            while t and ord(t[-1])<=check_smallest_string():
                res+=(t.pop())
            pos+=1
        return res