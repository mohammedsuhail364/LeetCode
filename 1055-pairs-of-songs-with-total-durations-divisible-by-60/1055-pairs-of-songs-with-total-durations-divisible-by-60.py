class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cache=defaultdict(int)
        res=0
        for t in time:
            rem=t%60
            complement=(60-t)%60
            res+=cache[complement]
            cache[rem]+=1
        return res
        