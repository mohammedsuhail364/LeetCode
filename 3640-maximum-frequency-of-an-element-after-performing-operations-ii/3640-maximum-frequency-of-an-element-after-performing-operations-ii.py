class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        freq=Counter(nums)
        interval_change=defaultdict(int)
        for n in nums:
            start=n-k
            end=n+k+1
            interval_change[start]+=1
            interval_change[end]-=1
        points=sorted(freq.keys()|interval_change.keys())
        res=0
        active_intervals=0
        for p in points:
            active_intervals+=interval_change[p]
            curr_count=freq[p]
            # Between these points, active_intervals stays the same.
            extra=min(active_intervals-curr_count,numOperations)
            res=max(res,extra+curr_count)
        return res