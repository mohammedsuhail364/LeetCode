class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # refer this https://www.youtube.com/watch?v=FcWK8CJReUo
        def distance(p1,p2):
            return((p1[0]-p2[0])**2 + ((p1[1]-p2[1])**2 ))
        res=inf
        points_set=set(map(tuple,points))
        seen=set()
        for p1 in points_set:
            for p2 in seen:
                if p1==p2:
                    continue
                for p3 in seen:
                    if p1==p3 or p2==p3:
                        continue
                    # use pythogoras theoram
                    if distance(p1,p2)+distance(p2,p3)!=distance(p1,p3):
                        continue
                    # x1+x3=x2+x4 -> basic rectangle formula => x4=x1+x3-x2 
                    # y1+y3=y2+y4 -> basic rectangle formula => y4=y1+y3-y2
                    x4=p1[0]+p3[0]-p2[0]
                    y4=p1[1]+p3[1]-p2[1]
                    if(x4,y4) in seen:
                        length=sqrt(distance(p1,p2))
                        width=sqrt(distance(p2,p3))
                        area=length*width
                        res=min(res,area)
            seen.add(p1)
        return res if res!=inf else 0
