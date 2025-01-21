class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        li={}
        for i in nums:
            if i not in li:
                li[i]=1
            else:
                li[i]+=1
        for key,value in li.items():
            if value==1:
                return key

        