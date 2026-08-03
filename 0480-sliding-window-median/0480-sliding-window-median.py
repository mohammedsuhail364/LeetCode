class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def clean():
            while lowerHalf and remove.get(-lowerHalf[0],0)>0:
                remove[-lowerHalf[0]]-=1
                heappop(lowerHalf)
            while upperHalf and remove.get(upperHalf[0],0)>0:
                remove[upperHalf[0]]-=1
                heappop(upperHalf)
        def getMedian():
            if k%2:
                return -lowerHalf[0]/1.0
            return (-lowerHalf[0]+upperHalf[0])/2.0
        lowerHalf=[] # contains negatives maxHeap
        upperHalf=[] # contains postivies minHeap
        remove=defaultdict(int)
        res=[]
        for i in range(k):
            heappush(lowerHalf,-nums[i])
            heappush(upperHalf,-heappop(lowerHalf))
            # balance the two arrays 
            # main goal is to get the median from the sorted window array
            # if k is odd then lowerHalf size is greater than upperHalf
            # when k is odd then get the lowerHalf[0] 
            # when k is even then get the (lowerHalf[0]/upperHalf[0])/2
            if len(upperHalf)>len(lowerHalf):
                heappush(lowerHalf,-heappop(upperHalf))
        m=getMedian()
        res.append(m)
        n=len(nums)
        for i in range(k,n):
            out=nums[i-k]
            remove[out]+=1 # for lazy deletion
            # in this line we can get out is in the lower or upper , if -1 gets then it is lower else it was in the upper
            balance = -1 if out <= m else 1
            # now we find the incoming element is go in the lower or upper , now it is reverse if the nums[i]<=median then add in the lower else upper
            if nums[i]<=m:
                balance+=1
                heappush(lowerHalf,-nums[i])
            else:
                balance-=1
                heappush(upperHalf,nums[i])
            if balance<0: # we need balance for lower so we can get the upper half value and put in the lower half
                heappush(lowerHalf,-heappop(upperHalf))
            elif balance>0:
                heappush(upperHalf,-heappop(lowerHalf))
            clean()
            m=getMedian()
            res.append(m)
        return res