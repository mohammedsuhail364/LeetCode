class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols=(len(encodedText)//rows)
        curr_row=0
        curr_col=0
        r=0
        c=0
        res=''
        encodedTextNew=[[] for _ in range(rows)]
        curent_row=-1
        for i in range(len(encodedText)):
            if i%cols ==0:
                curent_row+=1
            encodedTextNew[curent_row].append(encodedText[i])
            
        
        while curr_row<rows and curr_col<cols:
            r=curr_row
            c=curr_col
            while r<rows and c<cols:
                res+=encodedTextNew[r][c]
                r+=1
                c+=1
            curr_row=0
            curr_col+=1
        return res.rstrip()