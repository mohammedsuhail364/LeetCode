from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        res=[]
        while i<len(firstList) and j<len(secondList):    
            s=max(firstList[i][0],secondList[j][0])
            e=min(firstList[i][1],secondList[j][1])
            if s<=e:
                res.append([s,e])
            if firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                j+=1
        return res