class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        pair=sorted(freq.items(),reverse=True,key=lambda x:x[1])
        res=''
        for i,j in pair:
            res+=i*j
        return res