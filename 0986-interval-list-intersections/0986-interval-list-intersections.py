class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        res=[]
        while i<len(firstList) and j<len(secondList):
            first=firstList[i]
            second=secondList[j]
            
            temp=[max(first[0],second[0]),min(first[1],second[1])]
            if temp[0]<=temp[1]:
                res.append(temp)
            if first[1]<second[1]:
                i+=1
            else:
                j+=1
        return res