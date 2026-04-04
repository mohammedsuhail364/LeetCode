class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols=(len(encodedText)//rows)
        res=[]
        for start_col in range(cols):
            r=0
            c=start_col
            while r<rows and c<cols:
                res.append(encodedText[r*cols+c])
                r+=1
                c+=1
        return ''.join(res).rstrip()