class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo={}
        def dfs(i,one_cnt,zero_cnt):
            if (i,one_cnt,zero_cnt) in memo:
                return memo[(i,one_cnt,zero_cnt)]
            if i>=len(strs):
                return 0
            # skip the current one
            skip=dfs(i+1,one_cnt,zero_cnt)
            # include the current one
            include=0
            zeros=strs[i].count('0')
            ones=strs[i].count("1")
            if zero_cnt+zeros<=m and one_cnt+ones<=n:
                include = 1 + dfs(i+1,one_cnt+strs[i].count("1"),zero_cnt+strs[i].count('0'))
            memo[(i,one_cnt,zero_cnt)] = max(skip,include)
            return memo[(i,one_cnt,zero_cnt)]
        return dfs(0,0,0)
            