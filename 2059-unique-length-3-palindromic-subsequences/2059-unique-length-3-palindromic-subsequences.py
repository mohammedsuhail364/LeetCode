class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res=set()
        left=set()
        right=Counter(s)
        for mid in s:
            right[mid]-=1
            for c in left:
                if right[c] > 0:
                    res.add((mid,c))
            left.add(mid)
        return len(res)