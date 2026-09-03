class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        fuel=startFuel
        heap=[]
        count=0
        stations.append([target,0]) # which indicates we can reach target if we pop this 
        while stations:
            if fuel>=target:return count
            while stations and stations[0][0]<=fuel: # where we max to go , we get all the fuels and add in the max_heap and get the max value from that
                heappush_max(heap,stations[0][1])
                stations.pop(0)
            if not heap:return -1
            fuel+=heappop_max(heap)
            count+=1
        return count