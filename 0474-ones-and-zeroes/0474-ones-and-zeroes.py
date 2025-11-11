class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def dfs(i,zero,one):
            if i>=len(strs) or zero>m or one>n:
                return 0
            # skip the current one
            skip=dfs(i+1,zero,one)
            # include the current one
            count_zero=(strs[i].count("0")+zero)
            count_one=(strs[i].count("1")+one)
            include=0
            if count_zero<=m and count_one<=n:
                include=1+dfs(i+1,count_zero,count_one)
            return max(skip,include)
        return dfs(0,0,0)