class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res=[0]*n
        for s,e,inc in bookings:
            res[s-1]+=inc
            if e<n:
                res[e]-=inc
        for i in range(1,len(res)):
            res[i]=res[i-1]+res[i]
        return res