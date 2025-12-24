class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda i:(abs(i-x),i))
        res=sorted(arr[:k])
        return res
        