class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # this question same as the longest increasing subsequece just add the count list 
        # and also i m only do the table DP which is the LIS last form 
        # add the count and return Number of Longest Increasing Subsequence
        n=len(nums)
        dp=[[0]*(n+1) for _ in range(n+2)] # +2 for base row
        count=[[0]*(n+1) for _ in range(n+2)]
        # base case: when i == n, length = 0, ways = 1
        for p in range(n+1):
            count[n][p]=1
        for i in range(n-1,-1,-1):
            for prev in range(i-1,-2,-1):
                # why prev range is i-1 to -1 it indicates the previous index of the i
                p=prev+1 # this is because we cannot use the -1 as index just convert to 0
                # skip the current one
                dp[i][p]=dp[i+1][p]
                count[i][p]=count[i+1][p]
                # include the current one
                if prev==-1 or (prev!=-1 and nums[prev]<nums[i]):
                    include_len=1+dp[i+1][i+1]
                    include_cnt=count[i+1][i+1]
                    if include_len>dp[i][p]:
                        dp[i][p]=1+dp[i+1][i+1]
                        count[i][p]=include_cnt
                    elif include_len==dp[i][p]:
                        count[i][p]+=include_cnt
                    # why there is two i+1 first is as usual check the next index and second i+1 refers the in the backtrack solution we send the current i as the prev this is also for that but i+1 because 
                    # Recall the index shift rule: p = prev + 1, so to look up a state with prev = i, you use column i + 1.
                    # So dp[i+1][i+1] means:

                    # Row i+1 → next index (start from i+1)
                    # Column i+1 → prev is i (because p = prev + 1 = i + 1)

                    # When you include nums[i], the new "prev" becomes i. So the next call is dfs(i+1, prev=i) → table lookup is dp[i+1][i+1]. 
        return count[0][0]
                
                