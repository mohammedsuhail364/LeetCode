class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache={}
        def backtrack(i,prev):
            if i==len(nums):
                return []
            if (i,prev) in cache:
                return cache[(i,prev)]
            res=backtrack(i+1,prev)
            if nums[i]%prev==0:
                temp=[nums[i]]+backtrack(i+1,nums[i])
                res=temp if len(temp)>len(res) else res
            cache[(i,prev)]=res
            return res
        return backtrack(0,1)