class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def binary_search(l,r,target):
            while l<=r:
                m=(l+r)//2
                if nums[m]>=target:
                    r=m-1
                else:
                    l=m+1
            return r
        res=0
        nums.sort()
        for i in range(len(nums)):
            low=lower-nums[i]
            up=upper-nums[i]
            res+=(binary_search(i+1,len(nums)-1,up+1)-binary_search(i+1,len(nums)-1,low))
        return res