class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff=[0]*n
        for s,e,inc in bookings:
            diff[s-1]+=inc
            if e<n:
                diff[e]-=inc
        for i in range(1,len(diff)):
            diff[i]+=diff[i-1]
        return diff
