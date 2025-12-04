class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res=[]
        n=len(nums)
        sorted_list=SortedList([])
        # add the k elements
        for i in range(k):
            sorted_list.add(nums[i])
        # iterate all the elements
        for i in range(k,n):
            if x<=len(sorted_list) and sorted_list[x-1]<0:
                res.append(sorted_list[x-1])
            else:
                res.append(0)
            sorted_list.remove(nums[i-k])
            sorted_list.add(nums[i])
        # handle the last k elements
        if x<=len(sorted_list) and sorted_list[x-1]<0:
            res.append(sorted_list[x-1])
        else:
            res.append(0)
        return res