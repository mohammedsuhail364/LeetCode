import bisect
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # res=[0]*len(nums)
        # for i in range(len(nums)):
        #     x=0
        #     for j in range(i+1,len(nums)):
        #         if nums[j]<nums[i]:
        #             x+=1
        #     res[i]=x
        # return res
        res=[]
        sorted_list=[]
        for num in reversed(nums):
            insert_pos=bisect.bisect_left(sorted_list,num)
            res.append(insert_pos)
            bisect.insort(sorted_list,num)
        return res[::-1]