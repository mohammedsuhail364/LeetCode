class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for i,j in Counter(nums).items():
            if j==2:
                res.append(i)
        return res