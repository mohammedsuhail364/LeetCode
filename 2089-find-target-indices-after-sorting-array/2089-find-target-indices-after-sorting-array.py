class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        cnt1 = 0
        cnt2 = 0
        for i in nums:
            if i < target:
                cnt1+=1
            elif i == target:
                cnt2+=1
        res=list(range(cnt1,cnt1+cnt2))
        return res