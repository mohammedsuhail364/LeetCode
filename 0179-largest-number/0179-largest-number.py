class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        li=[]
        for i in nums:
            li.append(str(i))
        li.sort(key=lambda x:x*10,reverse=True)
        if li[0]=='0':
            return '0'
        return ''.join(li)