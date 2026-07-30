class Solution:
    def minimumPushes(self, word: str) -> int:
        push=1
        c=0
        res=0
        for c in range(1,len(word)+1):
            res+=push
            if c%8==0:
                push+=1
        return res