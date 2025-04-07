class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum=sum(nums)
        if total_sum%2:
            return False
        target=total_sum//2
        dp=set()
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            next_dp=set()
            for t in dp:
                if t+nums[i]==target:
                    return True
                next_dp.add(t)
                next_dp.add(t+nums[i])
            dp=next_dp
        return True if target in dp else False

        