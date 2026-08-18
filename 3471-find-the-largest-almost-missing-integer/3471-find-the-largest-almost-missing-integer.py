class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k==n:
            return max(nums)
        c=Counter(nums)
        if k==1:
            res=[k for k,v in c.items() if v==1]
            if res:
                return max(res)
            return -1
        x=c[nums[0]]
        y=c[nums[-1]]
        if x==1 and y==1:
            return max(nums[0],nums[-1])
        if x==1:
            return nums[0]
        if y==1:
            return nums[-1]
        return -1