import heapq
class Solution:
    def minOperations(self, nums, k: int) -> int:
        heapq.heapify(nums)
        c=0
        flag=False
        while True:
            flag=False
            for x in nums:
                if x<k:
                    flag=True
                    break
            if flag:
                c+=1
                min_val=heapq.heappop(nums)
                max_val=heapq.heappop(nums)
                val=min_val*2+max_val
                heapq.heappush(nums,val)
            else:
                return c