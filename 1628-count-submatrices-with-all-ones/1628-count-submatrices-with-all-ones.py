class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows=len(mat)
        cols=len(mat[0])
        col=[]
        row=[]
        for r in range(rows):
            tmp=[]
            for c in range(cols):
                if r>0 and mat[r][c]:
                    val=col[-1][c]+1
                    tmp.append(val)
                else:
                    tmp.append(mat[r][c])
            col.append(tmp)
        res=0
        for r in range(rows):
            for c in range(cols):
                if not col[r][c]:
                    continue
                min_h=col[r][c]
                k=c
                while k>=0 and mat[r][k]>0:
                    min_h=min(min_h,col[r][k])
                    res+=min_h
                    k-=1  
        return res