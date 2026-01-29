class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre_sum=[0]
        for n in nums:
            pre_sum.append(pre_sum[-1]+n)
        print(pre_sum)
        for i in range(len(nums)):
            if pre_sum[i]==pre_sum[-1]-pre_sum[i+1]:
                return i
        return -1