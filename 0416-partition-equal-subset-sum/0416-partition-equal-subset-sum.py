class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False
        target=total//2
        dp=set()
        dp.add(0) # base case
        for i in range(len(nums)-1,-1,-1):
            next_dp=set()
            for x in dp:
                if x+nums[i]==target:
                    return True
                next_dp.add(x)
                next_dp.add(x+nums[i])
            dp=next_dp
        return False