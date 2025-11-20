class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1],-x[0]))
        choosen=[]
        for l,r in intervals:
            c=0
            for x in choosen:
                if l<=x<=r:
                    c+=1
            if c>=2:
                continue
            elif c==1:
                choosen.append(r)
            elif c==0:
                choosen.append(r-1)
                choosen.append(r)
        return len(choosen)