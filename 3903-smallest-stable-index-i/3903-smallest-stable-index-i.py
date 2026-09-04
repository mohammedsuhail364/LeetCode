class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        preMax=[nums[0]]
        for i in range(1,len(nums)):
            preMax.append(max(preMax[-1],nums[i]))
        postMin=[nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            postMin.append(min(postMin[-1],nums[i]))
        postMin=postMin[::-1]
        for i in range(len(nums)):
            x=preMax[i]-postMin[i]
            if x<=k:
                return i
        return -1