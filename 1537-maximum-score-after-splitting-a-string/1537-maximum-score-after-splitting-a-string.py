class Solution:
    def maxScore(self, s: str) -> int:
        def check(li):
            zero=0
            one=0
            for x in li:
                if x=='0':
                    zero+=1
                else:
                    one+=1
            return [zero,one]
        res=0
        for i in range(1,len(s)):
            zero,one=check(s[:i])
            zero_1,one_1=check(s[i:])
            res=max((zero+one_1),res)
        return res