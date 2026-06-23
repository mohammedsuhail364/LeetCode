class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # refer striver
        # this is under the partition DP
        # we want make the cuts as sorted and take the cuts according to this why because of sort we can make subproblems if not sorted sub problems depend on the another sub problem
        cuts=[0]+cuts+[n] 
        # this gives the formula to find out the length of the stick 
        # cuts[j+1]-cuts[i-1]
        cuts.sort()
        cache={}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[i,j]
            if i>j:
                return 0 # there is no partition to find
            cache[i,j]=inf
            for k in range(i,j+1):
                cost=cuts[j+1]-cuts[i-1] + dfs(i,k-1) + dfs(k+1,j)
                cache[i,j]=min(cost,cache[i,j])
            return cache[i,j]

        return dfs(1,len(cuts)-2)