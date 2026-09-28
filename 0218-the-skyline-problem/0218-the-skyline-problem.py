class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # refer this https://www.youtube.com/watch?v=ptbs99c9kl8&t=164s
        maxHeap=[0] # 0 -> grounded
        heights=[]
        for s,e,h in buildings:
            heights.append((s,-h)) # for the sorting purpose if the start and end are same we get the start first by this negative value
            heights.append((e,h))
        heights.sort()
        curMax=0
        remove = defaultdict(int)
        res=[]
        for event,h in heights:
            if h<0:
                heappush(maxHeap,h)
            else:
                remove[-h]+=1
            while maxHeap and remove[maxHeap[0]]>0:
                remove[maxHeap[0]]-=1
                heappop(maxHeap)
            maxVal = -maxHeap[0]
            if curMax != maxVal:
                res.append([event,maxVal])
                curMax = maxVal
        return res