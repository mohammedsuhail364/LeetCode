class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap=[]
        for n in nums:
            if min_heap and len(min_heap)>k:
                heappop(min_heap)
            heappush(min_heap,n)
        if min_heap and len(min_heap)>k:
            heappop(min_heap)
        return heappop(min_heap)