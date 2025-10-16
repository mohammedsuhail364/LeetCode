class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq=Counter([n%value for n in nums])
        i=0
        while True:
            rem=i%value
            if freq[rem]>0:
                freq[rem]-=1
                i+=1
            else:
                return i