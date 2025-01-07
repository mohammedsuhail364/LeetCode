class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        li=[]
        while nums:
            li.append(heapq.heappop(nums))
        return li