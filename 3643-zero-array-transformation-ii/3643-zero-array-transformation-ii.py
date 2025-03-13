class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n=len(nums)
        def make_array(k):
            diff=[0]*(n+1)
            for i in range(k):
                l,r,v=queries[i]
                diff[l]+=v
                diff[r+1]-=v
            cur_sum=0
            for i in range(n):
                cur_sum+=diff[i]
                if cur_sum<nums[i]:
                    return False
            return True
        if all(x==0 for x in nums):
            return 0
        l=1
        r=len(queries)
        if not make_array(r):
            return -1
        while l<r:
            mid=l+(r-l)//2
            if make_array(mid):
                r=mid
            else:
                l=mid+1
        return l