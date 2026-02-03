class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # refer neetcode
        ROWS=len(matrix)
        COLS=len(matrix[0])
        pre_sum=[[0]*COLS for i in range(ROWS)]
        res=0
        for r in range(ROWS):
            for c in range(COLS):
                top=pre_sum[r-1][c] if r>0 else 0
                left=pre_sum[r][c-1] if c>0 else 0
                top_left=pre_sum[r-1][c-1] if min(r,c)>0 else 0
                pre_sum[r][c]=matrix[r][c]+top+left-top_left
        for r1 in range(ROWS):
            for r2 in range(r1,ROWS):
                count=defaultdict(int)
                count[0]=1
                for c in range(COLS):
                    cur_sum=pre_sum[r2][c]-(pre_sum[r1-1][c] if r1>0 else 0)
                    diff = cur_sum - target
                    res+=count[diff]
                    count[cur_sum]+=1
        return res