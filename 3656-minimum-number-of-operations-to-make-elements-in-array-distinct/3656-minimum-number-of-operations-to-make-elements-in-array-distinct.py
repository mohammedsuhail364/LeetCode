class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        flag=True
        res=0
        while flag:
            if len(nums)==len(set(nums)):
                flag=False
            
            else:
                nums=nums[3:]
                res+=1
        return res