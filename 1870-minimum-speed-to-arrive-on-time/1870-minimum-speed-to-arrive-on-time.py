class Solution:
    def minSpeedOnTime(self, dist, hour: float) -> int:
        # Ceiling the last train’s time is wrong because arrival does not need to align to an integer hour.”
        l=1
        r=10**7 # ensure we always start with large numbers
        res=inf
        n=len(dist)
        while l<=r:
            speed=(l+r)//2
            hrs=0
            for i in range(n-1): # we dont want to include the last train for ceil process because it does not need because look this 
                # dist = [1, 1]
                # hour = 1.5
                # Try speed = 2
                # ceil(1/2) = 1
                # ceil(1/2) = 1
                # Total time = 2 ❌ (too late)
                # So this logic says:
                # speed = 2 ❌
                # First train: ceil(1/2) = 1
                # Last train:  1/2 = 0.5
                # Total = 1.5 ✅
                # speed = 2 ✅
                hrs+=ceil(dist[i]/speed)
            # for last train
            hrs+=dist[-1]/speed
            if hrs<=hour:
                res=min(res,speed)
                r=speed-1
            else:
                l=speed+1
        return res if res!=inf else -1