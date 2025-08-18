class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def helper(nums):
            if len(nums)==1:
                return abs(nums[0]-24)<1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i==j:
                        continue
                    a,b=nums[i],nums[j]
                    next_nums=[nums[k] for k in range(len(nums)) if k!=i and k!=j]
                    results=[a+b,a-b,a*b]
                    if abs(b)>1e-6:
                        results.append(a/b)
                    for val in results:
                        if helper(next_nums+[val]):
                            return True
            return False
        return helper([float(i) for i in cards])
