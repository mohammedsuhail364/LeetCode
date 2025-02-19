class Solution:
    def transpose(self, matrix) :
        rows=len(matrix)
        cols=len(matrix[0])
        res=[ [] for i in range(cols)]
        i=0
        j=0
        x=0
        while True:
            if j==cols:
                break
            if i==rows:
                j+=1
                i=0
                x+=1
                continue
            res[x].append(matrix[i][j])
            i+=1
            
        return res