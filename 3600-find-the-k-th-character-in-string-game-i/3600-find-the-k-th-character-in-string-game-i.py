class Solution:
    def kthCharacter(self, k: int) -> str:
        s=["a"]
        while len(s)<=k+1:
            for i in range(len(s)):
                val=s[i]
                if val=='z':
                    s.append("a")
                else:
                    s.append(chr(ord(val)+1))
        return s[k-1]