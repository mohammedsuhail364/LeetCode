from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        new_s=Counter(s)
        new_t=Counter(t)
        c=0
        for char in set(new_s.keys()).union(new_t.keys()):
            c+=abs(new_s[char]-new_t[char])
        return c