class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones=0
        res=0
        for i in nums:
            if i==1:
                ones+=1
            else:
                res=max(res,ones)
                ones=0
        res=max(res,ones)
        return res