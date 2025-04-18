class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=1
        arr=set(arr)
        count=0
        while count<k:
            if i not in arr:
                count+=1
            if count==k:
                return i
            i+=1

