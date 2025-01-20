class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows=len(mat)
        cols=len(mat[0])
        value_pos={}
        for r in range(rows):
            for c in range(cols):
                value_pos[mat[r][c]]=(r,c)
        row_counts=[0]*rows
        col_counts=[0]*cols
        for i in range(len(arr)):
            r,c=value_pos[arr[i]]
            row_counts[r]+=1
            col_counts[c]+=1
            if row_counts[r]==cols or col_counts[c]==rows:
                return i
        return -1
        