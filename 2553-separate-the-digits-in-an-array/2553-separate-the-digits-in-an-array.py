class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            temp=[]
            while num:
                temp.append(num%10)
                num=num//10
            res+=temp[::-1]
        return res