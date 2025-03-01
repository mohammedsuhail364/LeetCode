class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        li=[]
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                li.append(2*nums[i])
                li.append(0)
                i+=1
            else:
                li.append(nums[i])
            i+=1
        if len(li)!=len(nums):
            li.append(nums[-1])
        nums=[]
        zero=[]
        for x in li:
            if x==0:
                zero.append(x)
            else:
                nums.append(x)
        return nums+zero