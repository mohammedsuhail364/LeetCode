class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap=[]
        def gain(i,j):
            return (i+1)/(j+1)-(i/j) 
        for i,j in classes:
            heappush(heap,(-gain(i,j),i,j))
        while extraStudents:
            val,i,j=heappop(heap)
            i+=1
            j+=1
            extraStudents-=1
            heappush(heap,(-gain(i,j),i,j))
        res=0
        while heap:
            _,i,j=heappop(heap)
            res+=(i/j)
        return res/len(classes)