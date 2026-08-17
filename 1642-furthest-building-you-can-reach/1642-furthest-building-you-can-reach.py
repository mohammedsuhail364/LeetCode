class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # refer neetcode 
        # logic is every time we see the height we can use the bricks and store in the max heap if bricks are done we can use the ladder if we have , get the value from the max heap and add to the bricks that means we can use the ladder for that brick because ladder is super power we can jump any number so we can use the ladder for the existing brick we used and add that in the bricks
        max_heap=[]
        for i in range(len(heights)-1):
            diff=heights[i+1]-heights[i]
            if diff<=0:
                continue
            bricks-=diff
            heappush_max(max_heap,diff)
            if bricks<0: # we exceed the bricks count what we have
                # check we have ladder
                if ladders==0:
                    return i # we cannot cross this height
                ladders-=1
                # we get the max bricks from the max_heap
                bricks+=heappop_max(max_heap)
        return len(heights)-1 # we can reach the last one if we come 