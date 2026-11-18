class Solution:
    def minChanges(self, s: str) -> int:
        # just to check every 2 char is same or not
        res=0
        for i in range(0,len(s),2):
            if s[i]!=s[i+1]:res+=1
        return res