class Solution:
    def maximumTotalDamage(self, power) -> int:
        count=Counter(power)
        unique=sorted(count.keys())
        memo={}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i>=len(unique):
                return 0
            # this checks the every power as a starting point
            res=dfs(i+1)
            # include the valid ones
            j=i+1
            while j<len(unique) and unique[j]-unique[i]<=2:
                j+=1
            res=max(res,count[unique[i]]*unique[i]+dfs(j))
            memo[i]=res
            return res
            
        return dfs(0) 