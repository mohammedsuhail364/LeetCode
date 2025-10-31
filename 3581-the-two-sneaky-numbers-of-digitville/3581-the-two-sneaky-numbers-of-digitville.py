class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # refer neetcode
        res=0
        for n in nums:
            res^=n
        for i in range(len(nums)-2):
            res^=i
        res=res&-res
        xor1,xor2=0,0
        for n in nums:
            if n&res:
                xor1^=n
            else:
                xor2^=n
        for i in range(len(nums)-2):
            if i&res:
                xor1^=i
            else:
                xor2^=i
        return [xor1,xor2]

