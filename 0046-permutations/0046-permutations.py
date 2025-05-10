class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(perms):
            if len(perms)==len(nums):
                res.append(perms[:])
            for i in range(len(nums)):
                if nums[i] in perms:
                    continue
                perms.append(nums[i])
                dfs(perms)
                perms.pop()
        dfs([])
        return res