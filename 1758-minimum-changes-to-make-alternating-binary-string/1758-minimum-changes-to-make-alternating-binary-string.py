class Solution:
    def minOperations(self, s: str) -> int:
        # read the hints if you dont get 
        one=''
        zero=''
        tmp='1'
        for i in range(len(s)):
            one+=tmp
            tmp='0' if tmp=='1' else '1'
        tmp='0'
        for i in range(len(s)):
            zero+=tmp
            tmp='0' if tmp=='1' else '1'
        ones=0
        zeros=0
        for i in range(len(s)):
            if s[i]!=one[i]:
                ones+=1
            if s[i]!=zero[i]:
                zeros+=1
        return min(ones,zeros)
        