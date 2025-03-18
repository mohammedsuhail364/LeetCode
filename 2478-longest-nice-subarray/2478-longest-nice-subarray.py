class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        def check(li):
            for i in range(len(li)):
                for j in range(i+1,len(li)):
                    if (li[i]&li[j]) !=0:
                        return False
            return True
        res=1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                k=nums[i:j]
                if check(k):
                    res=max(res,len(k))
                else:
                    break
        return res