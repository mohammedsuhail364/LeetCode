class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seen=set(nums)
        n=len(nums)
        cur_max=0
        cur_max_len=0
        i=0
        while i<n:
            j=i
            cur_sum=nums[j]
            while j+1<n and nums[j+1]==nums[j]+1:
                cur_sum+=nums[j+1]
                j+=1
            cur_max=max(cur_sum,cur_max)
            break
        for x in range(cur_max,10000):
            if x not in seen:
                return x