class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        freq=Counter(nums)
        interval_change=defaultdict(int)
        for num in nums:
            start=num-k
            end=num+k+1
            interval_change[start]+=1
            interval_change[end]-=1
        points=sorted(interval_change.keys() | freq.keys())
        active_intervals=0
        res = 0 
        for point in points:
            active_intervals+=interval_change[point]
            curr_count=freq[point]
            extra=min(active_intervals-curr_count,numOperations)
            res=max(res,extra+curr_count)
        return res
