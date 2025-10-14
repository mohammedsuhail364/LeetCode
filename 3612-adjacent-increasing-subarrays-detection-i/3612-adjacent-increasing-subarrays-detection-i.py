class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def is_valid(arr):
            for i in range(1,len(arr)):
                if arr[i]<=arr[i-1]:
                    return False
            return True
        v=0
        i=k
        j=i+k
        while j<=len(nums):
            sub1=nums[v:i]
            sub2=nums[i:j]
            if is_valid(sub1) and is_valid(sub2):
                return True
            v+=1
            i+=1
            j+=1
        return False