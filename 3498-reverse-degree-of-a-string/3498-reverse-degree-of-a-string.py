class Solution:
    def reverseDegree(self, s: str) -> int:
        value=[i for i in range(26,0,-1)]
        # print(value)
        res=0
        for x,i in enumerate(s):
            index = ord(i) - ord('a')
            res+=(value[index]*(x+1))
        return res