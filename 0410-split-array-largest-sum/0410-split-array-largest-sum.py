class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        dp={}
        def dfs(i,m):
            if m==1:
                return sum(nums[i:])
            if (i,m) in dp:
                return dp[(i,m)]
            cur_sum=0
            res=inf
            for j in range(i,len(nums)-m+1):
                cur_sum+=nums[j]
                max_sum=max(cur_sum,dfs(j+1,m-1))
                res=min(res,max_sum)
                if cur_sum>res:
                    break
            dp[(i,m)]=res
            return dp[(i,m)]
        return dfs(0,k)