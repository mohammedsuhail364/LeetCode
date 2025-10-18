class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        used=set()
        cur=-inf
        for i in nums:
            start=max(i-k,cur+1)
            end=i+k
            if start<=end:
                used.add(start)
                cur=start
        return len(used)