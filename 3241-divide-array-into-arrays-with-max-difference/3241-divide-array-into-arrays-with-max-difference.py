class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        def check(li):
            if max(li)-min(li)>k:
                return False
            return True
        nums.sort()
        n=len(nums)//3
        res=[]
        l=0
        r=3
        for i in range(n):
            if check(nums[l:r]):
                res.append(nums[l:r])
            l+=3
            r+=3
        return res if len(res)==n else []
            