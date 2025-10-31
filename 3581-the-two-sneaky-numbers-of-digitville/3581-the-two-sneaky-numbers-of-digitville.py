class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [i for i,j in Counter(nums).items() if j==2]
        