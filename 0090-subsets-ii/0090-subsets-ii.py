class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=set()
        def dfs(temp,i):
            nonlocal res
            if i==len(nums):
                res.add(tuple(temp[:]))
                return
            temp.append(nums[i]) # include
            dfs(temp,i+1)
            temp.pop()
            dfs(temp,i+1)
        nums.sort()
        dfs([],0)
        return [list(s) for s in res]