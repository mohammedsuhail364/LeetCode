class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (-p[0], p[1])) 
        i=0
        res=0
        for i in range(len(points)):
            x,y=points[i]
            for j in range(i+1,len(points)):
                x1,y1=points[j]
                if x1<=x and y1>=y:
                    flag=True
                    for k in range(i+1,j):
                        _,y2=points[k]
                        if y<=y2<=y1:
                            flag=False
                            break
                    if flag:
                        res+=1
        return res