class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # refer this https://www.youtube.com/watch?v=fkSq0QE5C_0
        # this question basically asks us 
        # Core observation: If you shift img1 by (dr, dc), then a cell (r, c) in img1 lands on (r+dr, c+dc) in img2. So two 1s overlap iff:
        # img1[r1][c1] == 1 and img2[r2][c2] == 1
        # and (r2 - r1, c2 - c1) == (dr, dc)
        # So the question becomes: which translation vector (dr, dc) is shared by the most pairs of 1-cells?
        n=len(img1)
        ones1=[(r,c) for r in range(n) for c in range(n) if img1[r][c]]
        ones2=[(r,c) for r in range(n) for c in range(n) if img2[r][c]]
        shifts=defaultdict(int)
        for r1,c1 in ones1:
            for r2,c2 in ones2:
                dr,dc = (r2-r1,c2-c1)
                shifts[dr,dc]+=1
        return max(shifts.values()) if shifts else 0