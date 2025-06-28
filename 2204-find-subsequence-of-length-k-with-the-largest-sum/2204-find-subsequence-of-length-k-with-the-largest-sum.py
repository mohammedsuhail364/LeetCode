class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # pairing
        new_nums=[(num,i) for i,num in enumerate(nums)]
        # reverse sort 
        new_nums.sort(key=lambda x:-x[0])
        # make it sequence
        res=sorted(new_nums[:k],key=lambda x:x[1])

        return [r for r,_ in res]