class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def is_valid(max_allowed):
            sub_array=1
            cur_sum=0
            for n in nums:
                if cur_sum+n<=max_allowed:
                    cur_sum+=n
                else:
                    cur_sum=n
                    sub_array+=1
                    if sub_array>k:
                        return False
            return True
        # this is similiar to koko eating bananas and mainly same to 1011. Capacity To Ship Packages Within D Days
        # first we can set the range (max(nums),sum(nums)) why ? because if we start with 0 or 1 it is useless
        l=max(nums)
        r=sum(nums)
        res=0
        while l<=r:
            m=(l+r)//2
            # in this context m refers maximum value of split array we can check this is minimum of maximum
            if is_valid(m):
                res=m # find one of the value want to minimize this
                r=m-1
            else:
                l=m+1
        return res