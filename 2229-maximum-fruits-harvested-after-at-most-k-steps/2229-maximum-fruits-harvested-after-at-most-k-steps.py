class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        l=0
        max_f=0
        total=0
        for r in range(len(fruits)):
            total+=fruits[r][1]
            while l<=r:
                left_pos=fruits[l][0]
                right_pos=fruits[r][0]
                left_first=abs(startPos-left_pos)+(right_pos-left_pos)
                right_first=abs(startPos-right_pos)+(right_pos-left_pos)
                if min(left_first,right_first)<=k:
                    break
                total-=fruits[l][1]
                l+=1
            max_f=max(max_f,total)
        return max_f