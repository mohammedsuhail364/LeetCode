class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols=len(encodedText)//rows
        mat=defaultdict(list)
        x=0
        for r in range(rows):
            for c in range(cols):
                val=r-c
                mat[val].append(encodedText[x])
                x+=1
        res=[]
        for i in mat.values():
            res+=i
        return ''.join(res).rstrip()