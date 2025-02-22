class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        li=[]
        res=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                li.append(grid[i][j])
        
        for i in li:
            if li.count(i)>1:
                res.append(i)
                break
        for i in range(1,max(li)+2):
            if i in li:
                continue
            else:
                res.append(i)
                break
        return res