class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen=set()
        res=[]
        def dfs(i,path):
            if i>=len(nums):
                if tuple(path) not in seen:
                    res.append(path)
                    seen.add(tuple(path))
                return
            # include the current one
            dfs(i+1,path+[nums[i]])
            # skip the current one
            dfs(i+1,path)
        dfs(0,[])
        return list(res)