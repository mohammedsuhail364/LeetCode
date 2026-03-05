class Solution:
    def minOperations(self, s: str) -> int:
        # read the hints if you dont get 
        ones=0
        zeros=0
        tmp='1'
        for i in range(len(s)):
            if s[i]!=tmp:
                ones+=1
            tmp='0' if tmp=='1' else '1'
        tmp='0'
        for i in range(len(s)):
            if s[i]!=tmp:
                zeros+=1
            tmp='0' if tmp=='1' else '1'
        return min(ones,zeros)
        