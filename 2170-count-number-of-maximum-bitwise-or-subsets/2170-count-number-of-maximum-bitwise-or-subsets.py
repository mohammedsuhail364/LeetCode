class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n=len(nums)
        self.res=defaultdict(int)
        def backtrack(i,cur_or):
            if i == n:
                self.res[cur_or]+=1
                return
            # skip the current one
            backtrack(i+1,cur_or)
            # include the current one
            backtrack(i+1,cur_or | nums[i])
        backtrack(0,0)
        max_val=max(self.res)
        return self.res[max_val]