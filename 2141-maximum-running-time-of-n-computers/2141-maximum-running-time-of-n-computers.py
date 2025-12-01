class Solution:
    def maxRunTime(self, n: int, batteries) -> int:
        batteries.sort()
        low=0
        high=sum(batteries)//n
        def can_run(time):
            total=0
            for b in batteries:
                total+=min(b,time)
            return total>=time*n
        while low<high:
            mid=(low+high+1)//2
            if can_run(mid):
                low=mid
            else:
                high=mid-1
        return low
