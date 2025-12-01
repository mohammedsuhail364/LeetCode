class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0
        nums.sort()
        i=1
        tmp=1
        res=1
        prev=nums[0]
        while i<len(nums):
            if prev==nums[i]:
                i+=1
                continue
            if prev+1==nums[i]:
                prev=nums[i]
                tmp+=1
            else:
                res=max(res,tmp)
                tmp=1
                prev=nums[i]
            i+=1
        res=max(res,tmp)
        return res