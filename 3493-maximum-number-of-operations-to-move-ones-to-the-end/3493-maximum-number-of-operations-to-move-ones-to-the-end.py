class Solution:
    def maxOperations(self, s: str) -> int:
        count_ones=0
        res=0
        i=0
        while i<len(s):
            if s[i]=='1':
                count_ones+=1
                i+=1
            else:
                while i<len(s) and s[i]=='0':
                    i+=1
                res+=count_ones
        return res
