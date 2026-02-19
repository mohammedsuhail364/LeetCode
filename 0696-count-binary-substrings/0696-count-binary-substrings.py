class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # s = "00110011"
        # Groups:

        # "00" → 2
        # "11" → 2
        # "00" → 2
        # "11" → 2
        # So group lengths:

        # [2, 2, 2, 2]
        # Number of valid substrings =
        # min(group[i], group[i+1]) summed for all adjacent groups.

        # So:

        # min(2,2) + min(2,2) + min(2,2)
        # = 2 + 2 + 2
        # = 6
        res=0
        cur=1
        prev=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cur+=1
            else:
                res+=min(prev,cur)
                prev=cur
                cur=1
        res+=min(prev,cur)
        return res
            