class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        di={}
        li=[]
        for i in nums:
            if i not in di:
                di[i]=1
            else:
                di[i]+=1
        for key,value in di.items():
            if value==1:
                li.append(key)
        return li