class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count=0
        perm=combinations(arr,3)
        for i in perm:
            if a>=abs(i[0]-i[1]) and b>=abs(i[1]-i[2]) and c>=abs(i[0]-i[2]):
                count+=1
        return count