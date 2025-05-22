class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # refer techdose
        n=len(nums)
        used_query=[] # min_heap
        available_query=[] #max_heap
        queries.sort()
        query_pos=0
        applied_count=0
        for i in range(n):
            while query_pos<len(queries) and queries[query_pos][0]==i:
                end=queries[query_pos][1]
                heappush(available_query,-end)
                query_pos+=1
            nums[i]-=len(used_query)
            while nums[i]>0 and available_query and -available_query[0]>=i:
                end=-heappop(available_query)
                nums[i]-=1
                heappush(used_query,end)
                applied_count+=1
            if nums[i]>0:
                return -1
            while used_query and used_query[0]==i:
                heappop(used_query)
        return len(queries)-applied_count
