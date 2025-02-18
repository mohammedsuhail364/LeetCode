class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        l=0
        for i in range(2,len(nums)+1):
            for j in combinations(nums,i):
                k=j[0]
                for x in range(1,len(j)):
                    k^=j[x]
                l+=k
        return l+sum(nums)