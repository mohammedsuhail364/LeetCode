class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # refer neetcode
        prices=[inf]*n
        prices[src]=0
        for i in range(k+1):
            temp=prices[:]
            for s,d,p in flights:
                # not connected with src
                if prices[s]==inf:
                    continue
                if prices[s]+p<temp[d]:
                    temp[d]=prices[s]+p
            prices=temp
        return -1 if prices[dst]==inf else prices[dst]