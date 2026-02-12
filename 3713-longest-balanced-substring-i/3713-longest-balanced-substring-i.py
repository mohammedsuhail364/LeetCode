class Solution:
    def longestBalanced(self, s: str) -> int:
        def is_valid(count):
            return len(set(count.values()))==1
        res=0
        for i in range(len(s)):
            count=defaultdict(int)
            for j in range(i,len(s)):
                count[s[j]]+=1
                if is_valid(count):
                    res=max(res,j-i+1)
        return res
