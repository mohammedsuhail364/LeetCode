class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # refer neetcode
        if sum(nums)%k !=0:
            return False
        used=[False]*len(nums)
        target=sum(nums)//k
        nums.sort(reverse=True)
        if max(nums)>target:
            return False
        def dfs(i,k,curSum):
            if k==0:
                return True
            if curSum==target:
                return dfs(0,k-1,0)
            for j in range(i,len(nums)):
                if used[j] or curSum+nums[j]>target:
                    continue
                used[j]=True
                if dfs(j+1,k,curSum+nums[j]):
                    return True
                used[j]=False
                if curSum==0:
                    break
            return False

        return dfs(0,k,0)