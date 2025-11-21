class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # refer neetcode
        left=set()
        right=Counter(s)
        res=set()
        for m in s:
            right[m]-=1
            for c in left:
                if right[c]>0:
                    res.add((c,m)) # (left_char,middle_char)
            left.add(m)
        return len(res)