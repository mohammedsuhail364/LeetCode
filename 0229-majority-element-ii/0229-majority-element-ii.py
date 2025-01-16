class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        di=Counter(nums)
        res=[]
        check=len(nums)//3
        for i,j in di.items():
            if check<j:
                res.append(i)
        return res