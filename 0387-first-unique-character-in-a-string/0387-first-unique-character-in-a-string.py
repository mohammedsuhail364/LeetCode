class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq=Counter(s)
        for i,v in enumerate(s):
            if freq[v]==1:
                return i
        return -1