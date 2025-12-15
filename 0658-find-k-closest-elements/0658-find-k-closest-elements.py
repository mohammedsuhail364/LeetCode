class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pairs=[]
        for n in arr:
            pairs.append((abs(n-x),n))
        pairs.sort()
        res=[n for d,n in pairs[:k]]
        return sorted(res)