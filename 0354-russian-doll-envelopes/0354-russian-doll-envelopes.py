from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # this question is same variation of the Longest increasing subsequence with some tricks
        # trick one is sort with ascending width and decending height 
        # why because 
        # Using [[5,4],[6,4],[6,7],[2,3]]:
        # After sort → [[2,3],[5,4],[6,7],[6,4]]
        # Heights = [3, 4, 7, 4]
        # LIS = [3, 4, 7] → corresponds to envelopes [2,3],[5,4],[6,7]
        # Check widths: 2 < 5 < 6 ✓ strictly increasing!
        # No! Try [[6,4],[6,7]] with normal sort:
        # Heights = [4, 7] → LIS = 2 ❌ (same width, can't stack!)
        # STEPS 
        # 1.sort the envelopes 
        # 2.extract the height because we know width is ascending
        # 3. apply the LIS
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        heights=[h for w,h in envelopes]
        temp=[heights[0]]
        l=1
        for i in range(1,len(heights)):
            if heights[i]>temp[-1]:
                temp.append(heights[i])
                l+=1
            else:
                index=bisect_left(temp,heights[i])
                temp[index]=heights[i]
        return l