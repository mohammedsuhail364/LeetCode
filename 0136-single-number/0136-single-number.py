class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # s={}
        # for i in nums:
        #     if i not in s:
        #         s[i]=1
        #     else:
        #         s[i]+=1
        # for key,value in s.items():
        #     if value ==1:
        #         return key
        res=0
        for i in nums:
            res=res^i
        return res
