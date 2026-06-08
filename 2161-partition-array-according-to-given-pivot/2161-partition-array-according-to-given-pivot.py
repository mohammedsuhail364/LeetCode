class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low=[]
        high=[]
        middle=[]
        for i in nums:
            if i<pivot:
                low.append(i)
            elif i>pivot:
                high.append(i)
            else:
                middle.append(i)
        return low+middle+high