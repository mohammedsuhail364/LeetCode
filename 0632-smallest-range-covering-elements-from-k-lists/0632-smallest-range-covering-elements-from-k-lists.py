class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # this list contains (value,list_index,ele_index)
        min_heap=[]
        cur_max=-inf
        for i in range(len(nums)):
            heappush(min_heap,(nums[i][0],i,0))
            cur_max=max(cur_max,nums[i][0])
        res=[-inf,inf]
        while True:
            cur_min,list_idx,ele_idx=heappop(min_heap)
            if cur_max-cur_min<res[1]-res[0]:res=[cur_min,cur_max]
            if ele_idx + 1 >= len(nums[list_idx]):break
            next_idx = ele_idx + 1
            next_val=nums[list_idx][next_idx]
            heappush(min_heap,(next_val,list_idx,next_idx))
            cur_max=max(cur_max,next_val)
        return res
        
        