class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        pre_left=[0]
        pre_right=[0]
        for i in nums:
            pre_left.append(pre_left[-1]+i)
        print(pre_left)
        for i in range(len(nums)-1,-1,-1):
            pre_right.append(pre_right[-1]+nums[i])
        pre_right=pre_right[::-1]
        print(pre_right)
        res=0
        for i in range(len(nums)):
            if nums[i] != 0:
                continue
            if pre_left[i] == pre_right[i]:
                res += 2
            elif abs(pre_left[i] - pre_right[i]) == 1:
                res += 1
        return res
        