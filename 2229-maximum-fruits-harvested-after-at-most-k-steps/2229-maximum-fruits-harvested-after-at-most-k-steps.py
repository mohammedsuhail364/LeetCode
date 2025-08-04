from bisect import bisect_right
from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left, right = [], []
        
        # Split into left and right
        for pos, cnt in fruits:
            if pos <= startPos:
                left.append([startPos - pos, cnt])
            else:
                right.append([pos - startPos, cnt])
        
        left.reverse()  # Closest first
        
        # Precompute prefix sums
        pSumL = [0]*(len(left)+1)
        pSumR = [0]*(len(right)+1)
        for i, (_, cnt) in enumerate(left):
            pSumL[i+1] = pSumL[i] + cnt
        for i, (_, cnt) in enumerate(right):
            pSumR[i+1] = pSumR[i] + cnt

        # Precompute distance arrays for bisect
        left_dist = [d for d, _ in left]
        right_dist = [d for d, _ in right]

        def count_length(dist_list, steps):
            if steps < 0:
                return 0
            return bisect_right(dist_list, steps)

        max_collect = 0

        # Iterate over the smaller of k or fruit distances
        max_steps = min(k, max(left_dist[-1] if left else 0,
                               right_dist[-1] if right else 0))

        for i in range(max_steps + 1):
            # Go left first
            l_cnt = count_length(left_dist, i)
            r_cnt = count_length(right_dist, k - 2*i)
            max_collect = max(max_collect, pSumL[l_cnt] + pSumR[r_cnt])
            
            # Go right first
            r_cnt = count_length(right_dist, i)
            l_cnt = count_length(left_dist, k - 2*i)
            max_collect = max(max_collect, pSumL[l_cnt] + pSumR[r_cnt])

        return max_collect
